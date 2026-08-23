"""
TRAVELIQ — AI Travel Research & Smart Trip Planner
Core RAG (Retrieval-Augmented Generation) Pipeline
"""

import os
import re
import math
from typing import List, Dict, Any, Optional, Tuple
from dotenv import load_dotenv
import pypdf
import chromadb
from chromadb.utils import embedding_functions

# Load environment variables
load_dotenv()

# Configuration defaults
DEFAULT_CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 800))
DEFAULT_CHUNK_OVERLAP = int(os.environ.get("CHUNK_OVERLAP", 120))
DEFAULT_TOP_K = int(os.environ.get("TOP_K", 5))
RESEARCH_TOP_K = int(os.environ.get("RESEARCH_TOP_K", 8))
CHROMA_PERSIST_DIR = os.environ.get("CHROMA_PERSIST_DIR", "./vectorstore")
COLLECTION_NAME = "traveliq_knowledge_base"

# RAG System Prompts
TRAVELIQ_SYSTEM_PROMPT = """You are TRAVELIQ, an AI Travel Research Assistant.
Answer the user's question using ONLY the retrieved travel information provided in the context.
Do not invent attractions, rules, prices, opening hours, transportation details, or other facts that are not supported by the retrieved context.
If the context does not contain enough information, clearly say:
"I could not find enough information in the available travel sources."
When possible, mention the source filename and page number.
If the user requests a personalized itinerary, use the retrieved information together with the user's destination, duration, budget, and interests.
Do not claim exact prices unless the retrieved sources provide them.
Clearly distinguish information found in sources from assumptions or estimates."""


# -----------------------------------------------------------------------------
# STEP 2: PDF Document Extraction
# -----------------------------------------------------------------------------
def extract_text_from_pdf(filepath: str) -> List[Dict[str, Any]]:
    """
    Extract text page-by-page from a PDF file using PyPDF.
    Preserves:
      - filename
      - page_number (1-indexed)
      - text
    Returns a list of page dictionaries.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    if not filepath.lower().endswith(".pdf"):
        raise ValueError("Invalid file format. Only PDF files are supported.")

    filename = os.path.basename(filepath)
    extracted_pages = []
    total_text_length = 0

    try:
        reader = pypdf.PdfReader(filepath)
        num_pages = len(reader.pages)

        if num_pages == 0:
            raise ValueError(f"The PDF file '{filename}' is empty (0 pages).")

        for idx, page in enumerate(reader.pages):
            page_num = idx + 1
            raw_text = page.extract_text() or ""
            # Clean up whitespace while preserving sentences
            cleaned_text = re.sub(r"[ \t]+", " ", raw_text).strip()
            total_text_length += len(cleaned_text)

            if cleaned_text:
                extracted_pages.append({
                    "filename": filename,
                    "page_number": page_num,
                    "text": cleaned_text
                })

        if total_text_length < 20:
            raise ValueError(
                f"The PDF file '{filename}' contains no extractable text. "
                "It may be scanned or image-only without OCR text."
            )

        return extracted_pages

    except pypdf.errors.PdfStreamError as e:
        raise ValueError(f"Corrupted or invalid PDF file '{filename}': {str(e)}")
    except Exception as e:
        if isinstance(e, ValueError):
            raise
        raise RuntimeError(f"Error reading PDF '{filename}': {str(e)}")


# -----------------------------------------------------------------------------
# STEP 3: Text Chunking
# -----------------------------------------------------------------------------
def chunk_text(
    pages: List[Dict[str, Any]],
    chunk_size: int = DEFAULT_CHUNK_SIZE,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP
) -> List[Dict[str, Any]]:
    """
    Split extracted page text into overlapping chunks with source metadata.
    Preserves:
      - filename
      - page_number
      - chunk_id
      - text
    """
    chunks = []

    for page_data in pages:
        filename = page_data["filename"]
        page_num = page_data["page_number"]
        text = page_data["text"]

        if not text:
            continue

        if len(text) <= chunk_size:
            chunks.append({
                "chunk_id": f"{filename}_p{page_num}_c0",
                "text": text,
                "metadata": {
                    "filename": filename,
                    "page_number": page_num,
                    "chunk_index": 0
                }
            })
            continue

        # Split text intelligently using sentence/paragraph boundaries
        step = max(1, chunk_size - chunk_overlap)
        start = 0
        chunk_idx = 0

        while start < len(text):
            end = min(start + chunk_size, len(text))
            
            # If not at the end of the text, try to find a natural boundary near 'end'
            if end < len(text):
                boundary_found = -1
                # Look backwards up to chunk_overlap chars for sentence/paragraph endings
                search_sub = text[start:end]
                for delim in ["\n\n", ".\n", ". ", "!\n", "! ", "?\n", "? ", "\n", "; "]:
                    pos = search_sub.rfind(delim)
                    if pos != -1 and pos > (chunk_size // 2):
                        boundary_found = start + pos + len(delim)
                        break
                if boundary_found != -1:
                    end = boundary_found

            chunk_content = text[start:end].strip()
            if chunk_content:
                chunks.append({
                    "chunk_id": f"{filename}_p{page_num}_c{chunk_idx}",
                    "text": chunk_content,
                    "metadata": {
                        "filename": filename,
                        "page_number": page_num,
                        "chunk_index": chunk_idx
                    }
                })
                chunk_idx += 1

            if end >= len(text):
                break

            start += step

    return chunks


# -----------------------------------------------------------------------------
# STEP 4, 5, 6: Embeddings, Persistent ChromaDB & Retrieval
# -----------------------------------------------------------------------------
class TravelIQKnowledgeBase:
    """
    Manages vector embeddings and persistent ChromaDB storage for TravelIQ.
    Uses Sentence Transformers (all-MiniLM-L6-v2).
    """

    def __init__(self, persist_dir: str = CHROMA_PERSIST_DIR):
        self.persist_dir = persist_dir
        os.makedirs(self.persist_dir, exist_ok=True)

        # Initialize Embedding Function (all-MiniLM-L6-v2)
        try:
            self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
                model_name="all-MiniLM-L6-v2"
            )
        except Exception:
            # Fallback to Chroma's default ONNX implementation of all-MiniLM-L6-v2
            self.embedding_function = embedding_functions.DefaultEmbeddingFunction()

        # Initialize ChromaDB persistent client
        self.client = chromadb.PersistentClient(path=self.persist_dir)
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_function,
            metadata={"hnsw:space": "cosine"}
        )

    def add_chunks(self, chunks: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Store chunks and their metadata into ChromaDB.
        """
        if not chunks:
            return {"added": 0, "total": self.collection.count()}

        ids = [c["chunk_id"] for c in chunks]
        documents = [c["text"] for c in chunks]
        metadatas = [
            {
                "filename": str(c["metadata"]["filename"]),
                "page_number": int(c["metadata"]["page_number"]),
                "chunk_index": int(c["metadata"].get("chunk_index", 0))
            }
            for c in chunks
        ]

        # Use upsert to prevent duplication
        self.collection.upsert(
            ids=ids,
            documents=documents,
            metadatas=metadatas
        )

        return {
            "added": len(chunks),
            "total_chunks": self.collection.count()
        }

    def retrieve(self, query: str, top_k: int = DEFAULT_TOP_K) -> List[Dict[str, Any]]:
        """
        Convert query into embedding, search ChromaDB, and return top_k chunks.
        Preserves metadata (filename, page_number).
        """
        if not query or not query.strip():
            return []

        count = self.collection.count()
        if count == 0:
            return []

        actual_k = min(top_k, count)
        results = self.collection.query(
            query_texts=[query],
            n_results=actual_k,
            include=["documents", "metadatas", "distances"]
        )

        retrieved_chunks = []
        if results and "documents" in results and results["documents"]:
            docs = results["documents"][0]
            metas = results["metadatas"][0] if "metadatas" in results else []
            distances = results["distances"][0] if "distances" in results else []

            for i, doc in enumerate(docs):
                meta = metas[i] if i < len(metas) else {}
                dist = distances[i] if i < len(distances) else 0.0
                retrieved_chunks.append({
                    "text": doc,
                    "filename": meta.get("filename", "Unknown"),
                    "page_number": int(meta.get("page_number", 1)),
                    "distance": float(dist),
                    "similarity": round(1.0 - float(dist), 4) if dist is not None else 1.0
                })

        return retrieved_chunks

    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about stored documents, pages, and chunks.
        """
        count = self.collection.count()
        if count == 0:
            return {
                "documents": 0,
                "pages": 0,
                "chunks": 0,
                "files": []
            }

        # Fetch all metadatas to compute distinct file and page counts
        data = self.collection.get(include=["metadatas"])
        metas = data.get("metadatas", []) or []

        unique_files = set()
        unique_pages = set()

        for m in metas:
            if m and "filename" in m:
                unique_files.add(m["filename"])
                unique_pages.add(f"{m['filename']}_p{m.get('page_number', 1)}")

        return {
            "documents": len(unique_files),
            "pages": len(unique_pages),
            "chunks": count,
            "files": sorted(list(unique_files))
        }

    def list_documents(self) -> List[Dict[str, Any]]:
        """
        Return a detailed summary of all indexed documents.
        """
        count = self.collection.count()
        if count == 0:
            return []

        data = self.collection.get(include=["metadatas"])
        metas = data.get("metadatas", []) or []

        file_stats: Dict[str, Dict[str, Any]] = {}
        for m in metas:
            if not m or "filename" not in m:
                continue
            fn = m["filename"]
            pg = m.get("page_number", 1)
            if fn not in file_stats:
                file_stats[fn] = {"filename": fn, "pages": set(), "chunks": 0}
            file_stats[fn]["pages"].add(pg)
            file_stats[fn]["chunks"] += 1

        doc_list = []
        for fn, s in file_stats.items():
            doc_list.append({
                "filename": fn,
                "pages_count": len(s["pages"]),
                "chunks_count": s["chunks"]
            })

        return sorted(doc_list, key=lambda x: x["filename"])

    def clear_all(self):
        """
        Clear the Chroma collection.
        """
        self.client.delete_collection(name=COLLECTION_NAME)
        self.collection = self.client.get_or_create_collection(
            name=COLLECTION_NAME,
            embedding_function=self.embedding_function,
            metadata={"hnsw:space": "cosine"}
        )


# Global singleton instance of knowledge base
knowledge_base = TravelIQKnowledgeBase()


# -----------------------------------------------------------------------------
# STEP 7: Google Gemini LLM Integration
# -----------------------------------------------------------------------------
def get_gemini_client():
    """
    Retrieve configured Gemini API client.
    """
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is not configured. Please add your GEMINI_API_KEY to the .env file."
        )

    import google.generativeai as genai
    genai.configure(api_key=api_key)
    return genai


def format_sources(chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Extract unique, ordered source citations from retrieved chunks.
    """
    seen = set()
    sources = []
    for c in chunks:
        fn = c.get("filename", "Unknown")
        pg = c.get("page_number", 1)
        key = (fn, pg)
        if key not in seen and fn != "Unknown":
            seen.add(key)
            sources.append({
                "filename": fn,
                "page": pg,
                "citation": f"{fn} — Page {pg}"
            })
    return sources


def build_context_string(chunks: List[Dict[str, Any]]) -> str:
    """
    Build structured context string from retrieved chunks with clear source labels.
    """
    if not chunks:
        return "No relevant travel documents found in the knowledge base."

    context_parts = []
    for idx, c in enumerate(chunks, start=1):
        context_parts.append(
            f"--- SOURCE {idx}: [File: {c['filename']}, Page: {c['page_number']}] ---\n"
            f"{c['text']}"
        )
    return "\n\n".join(context_parts)


def call_gemini_with_fallback(prompt: str, system_instruction: Optional[str] = None) -> str:
    """
    Execute prompt against Gemini with model fallback.
    """
    genai = get_gemini_client()
    
    # Priority list of models
    models_to_try = [
        "gemini-1.5-flash",
        "gemini-2.0-flash",
        "gemini-1.5-pro",
        "gemini-pro"
    ]

    last_error = None
    for model_name in models_to_try:
        try:
            if system_instruction and ("1.5" in model_name or "2.0" in model_name):
                model = genai.GenerativeModel(
                    model_name=model_name,
                    system_instruction=system_instruction
                )
            else:
                model = genai.GenerativeModel(model_name=model_name)

            response = model.generate_content(
                prompt,
                generation_config={"temperature": 0.2, "top_p": 0.8}
            )
            if response and response.text:
                return response.text.strip()
        except Exception as e:
            last_error = e
            continue

    raise RuntimeError(f"Failed to generate response with Gemini models: {str(last_error)}")


def generate_answer(
    question: str,
    context_chunks: List[Dict[str, Any]],
    conversation_history: Optional[List[Dict[str, str]]] = None,
    preferences: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """
    Generate grounded answer to user question using retrieved chunks and Gemini.
    """
    if not question or not question.strip():
        raise ValueError("Question cannot be empty.")

    sources = format_sources(context_chunks)
    context_str = build_context_string(context_chunks)

    # Format conversation history
    history_str = ""
    if conversation_history:
        history_items = []
        for msg in conversation_history[-4:]:  # Keep last 4 messages for concise context
            role = "User" if msg.get("role") == "user" else "Assistant"
            history_items.append(f"{role}: {msg.get('content', '')}")
        if history_items:
            history_str = "Recent Conversation History:\n" + "\n".join(history_items) + "\n\n"

    # User preferences context
    pref_str = ""
    if preferences:
        parts = []
        if preferences.get("destination"):
            parts.append(f"Destination: {preferences['destination']}")
        if preferences.get("duration"):
            parts.append(f"Trip Duration: {preferences['duration']} days")
        if preferences.get("budget"):
            parts.append(f"Budget: ₹{preferences['budget']}")
        if preferences.get("interests"):
            interests = preferences["interests"]
            if isinstance(interests, list):
                parts.append(f"Interests: {', '.join(interests)}")
            else:
                parts.append(f"Interests: {interests}")
        if parts:
            pref_str = "User Trip Profile:\n" + "\n".join(parts) + "\n\n"

    prompt = f"""{history_str}{pref_str}RETRIEVED TRAVEL SOURCES CONTEXT:
{context_str}

USER QUESTION:
{question}

INSTRUCTIONS:
1. Answer the question using ONLY the facts present in the RETRIEVED TRAVEL SOURCES CONTEXT above.
2. If the context does not contain enough information to answer the question, clearly state:
"I could not find enough information in the available travel sources."
3. Mention source filenames and page numbers when referencing facts.
4. Do NOT hallucinate attractions, operating hours, prices, or policies not in the context.
5. If the user asks for a comparison or itinerary, organize it clearly with markdown formatting.
"""

    answer_text = call_gemini_with_fallback(
        prompt=prompt,
        system_instruction=TRAVELIQ_SYSTEM_PROMPT
    )

    return {
        "answer": answer_text,
        "sources": sources,
        "chunks_used": len(context_chunks)
    }


# -----------------------------------------------------------------------------
# STEP 12: Personalized Itinerary Generation
# -----------------------------------------------------------------------------
def generate_itinerary(
    destination: str,
    duration: int,
    budget: Optional[str],
    interests: List[str],
    context_chunks: List[Dict[str, Any]],
    conversation_history: Optional[List[Dict[str, str]]] = None,
    research_mode: bool = False
) -> Dict[str, Any]:
    """
    Generate a structured, personalized day-by-day travel plan grounded in retrieved sources.
    """
    if not destination or not destination.strip():
        raise ValueError("Destination is required to generate a travel plan.")

    sources = format_sources(context_chunks)
    context_str = build_context_string(context_chunks)

    interests_text = ", ".join(interests) if interests else "General sightseeing"
    budget_text = f"₹{budget}" if budget else "Not specified"

    prompt = f"""You are TRAVELIQ, creating a personalized travel plan.

TRIP DETAILS:
- Destination: {destination}
- Duration: {duration} Days
- Budget: {budget_text}
- User Interests: {interests_text}
- Research Mode: {'Active (In-depth analysis)' if research_mode else 'Standard'}

RETRIEVED TRAVEL SOURCES CONTEXT:
{context_str}

REQUIRED OUTPUT FORMAT:
Create a complete, realistic, structured travel plan grounded STRICTLY in the retrieved context:

# ✈️ {duration}-Day Personalized Itinerary for {destination}

## 🌟 Overview & Trip Alignment
(Brief summary of how this plan matches interests: {interests_text} and duration: {duration} days)

## 📅 Day-by-Day Itinerary

### DAY 1
- **Morning**: [Attraction / Activity based on sources] (Source: filename, Page X)
- **Afternoon**: [Attraction / Activity / Lunch spot based on sources] (Source: filename, Page X)
- **Evening**: [Attraction / Activity based on sources] (Source: filename, Page X)

(Repeat for each day up to DAY {duration})

## 💰 Budget Notes
(Only quote prices/costs if found in the sources. Clearly distinguish estimated expenses from documented costs.)

## ⚠️ Important Information & Travel Rules
(Entry rules, timings, dress codes, or permits mentioned in the documents)

## 💡 Practical Travel Tips
(Local advice, best time to visit, transportation tips found in the context)

## 📚 Sources Consulted
(List the document names and page numbers used)

STRICT GROUNDING RULES:
1. ONLY include attractions, historical landmarks, restaurants, beaches, and activities that exist in the RETRIEVED CONTEXT.
2. If certain days or slots cannot be populated because the sources lack information, explicitly mention that more details for that specific activity were not found in the uploaded documents.
3. Do NOT make up ticket prices or opening hours unless the source text states them.
"""

    answer_text = call_gemini_with_fallback(
        prompt=prompt,
        system_instruction=TRAVELIQ_SYSTEM_PROMPT
    )

    return {
        "plan": answer_text,
        "destination": destination,
        "duration": duration,
        "budget": budget,
        "interests": interests,
        "sources": sources,
        "chunks_used": len(context_chunks)
    }
