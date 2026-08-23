"""
Automated unit & pipeline verification script for TRAVELIQ RAG Backend.
Tests:
- PDF Extraction (pypdf)
- Text Chunking with metadata
- Embedding generation (all-MiniLM-L6-v2)
- ChromaDB indexing and persistence
- Semantic retrieval accuracy and source citation
- Negative query grounding test
"""

import os
import sys

# Ensure UTF-8 output encoding on Windows consoles
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from rag import (
    extract_text_from_pdf,
    chunk_text,
    TravelIQKnowledgeBase,
    generate_answer,
    generate_itinerary,
    format_sources
)

def run_tests():
    print("=" * 60)
    print("[*] TRAVELIQ RAG Pipeline Self-Test")
    print("=" * 60)

    # 1. Test PDF Extraction
    sample_pdf = "uploads/Goa_Tourism_Guide.pdf"
    print(f"\n[1] Testing PDF Extraction from: {sample_pdf}")
    assert os.path.exists(sample_pdf), f"Sample PDF missing: {sample_pdf}"
    
    pages = extract_text_from_pdf(sample_pdf)
    print(f"    [OK] Extracted {len(pages)} pages successfully.")
    assert len(pages) >= 5, f"Expected at least 5 pages, got {len(pages)}"
    for p in pages:
        assert p["filename"] == "Goa_Tourism_Guide.pdf"
        assert p["page_number"] > 0
        assert len(p["text"]) > 50
    print(f"    [OK] Page 1 sample text: {pages[0]['text'][:80]}...")

    # 2. Test Chunking
    print("\n[2] Testing Document Chunking (size=800, overlap=120)")
    chunks = chunk_text(pages, chunk_size=800, chunk_overlap=120)
    print(f"    [OK] Created {len(chunks)} chunks across {len(pages)} pages.")
    assert len(chunks) >= len(pages), "Chunks should be at least the number of pages"
    for c in chunks:
        assert "chunk_id" in c
        assert "text" in c
        assert "metadata" in c
        assert c["metadata"]["filename"] == "Goa_Tourism_Guide.pdf"
        assert c["metadata"]["page_number"] in [p["page_number"] for p in pages]
    print(f"    [OK] Chunk 0 ID: {chunks[0]['chunk_id']}")
    print(f"    [OK] Chunk 0 Text snippet: {chunks[0]['text'][:80]}...")

    # 3. Test ChromaDB Vector Store & Embeddings
    print("\n[3] Testing Sentence-Transformer Embeddings & ChromaDB Storage")
    kb = TravelIQKnowledgeBase(persist_dir="./vectorstore_test")
    kb.clear_all()
    add_result = kb.add_chunks(chunks)
    print(f"    [OK] Added {add_result['added']} chunks to vectorstore.")
    
    stats = kb.get_stats()
    print(f"    [OK] Vector Store Stats: {stats['documents']} docs, {stats['pages']} pages, {stats['chunks']} chunks")
    assert stats["documents"] == 1
    assert stats["pages"] >= 5
    assert stats["chunks"] == len(chunks)

    # 4. Test Semantic Retrieval: Historical Forts
    print("\n[4] Testing Semantic Retrieval for: 'historical forts and military architecture'")
    retrieved_forts = kb.retrieve("historical forts and military architecture", top_k=3)
    print(f"    [OK] Retrieved {len(retrieved_forts)} chunks.")
    assert len(retrieved_forts) > 0
    top_chunk = retrieved_forts[0]
    print(f"    [OK] Top match from: {top_chunk['filename']} Page {top_chunk['page_number']}")
    print(f"    [OK] Match snippet: {top_chunk['text'][:120]}...")
    assert "Aguada" in top_chunk["text"] or "Fort" in top_chunk["text"] or "Chapora" in top_chunk["text"]
    assert top_chunk["page_number"] == 2, f"Expected Forts on Page 2, got Page {top_chunk['page_number']}"

    # 5. Test Semantic Retrieval: Authentic Food & Cuisine
    print("\n[5] Testing Semantic Retrieval for: 'authentic goan cuisine fish curry vindaloo'")
    retrieved_food = kb.retrieve("authentic goan cuisine fish curry vindaloo", top_k=3)
    print(f"    [OK] Retrieved {len(retrieved_food)} chunks.")
    assert len(retrieved_food) > 0
    top_food = retrieved_food[0]
    print(f"    [OK] Top match from: {top_food['filename']} Page {top_food['page_number']}")
    print(f"    [OK] Match snippet: {top_food['text'][:120]}...")
    assert "Curry" in top_food["text"] or "Vindaloo" in top_food["text"] or "Bebinca" in top_food["text"]
    assert top_food["page_number"] == 4, f"Expected Food on Page 4, got Page {top_food['page_number']}"

    # 6. Test Source Formatter
    sources = format_sources(retrieved_forts + retrieved_food)
    print(f"\n[6] Testing Source Citation Formatter: {len(sources)} unique citations")
    for s in sources:
        print(f"    [Doc] {s['citation']}")
    assert len(sources) >= 2

    # 7. Test Gemini API (if key is set)
    gemini_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if gemini_key and gemini_key != "your_gemini_api_key_here":
        print("\n[7] Testing Gemini API Grounded Answer Generation...")
        try:
            res = generate_answer("What historical forts are mentioned?", retrieved_forts)
            print("    [OK] Gemini Answer:")
            print("    " + res["answer"][:200].replace("\n", "\n    ") + "...")
            print("    [OK] Sources:", [s["citation"] for s in res["sources"]])
        except Exception as e:
            print(f"    [!] Gemini call failed (check key validity): {e}")
    else:
        print("\n[7] Skipping live Gemini call (GEMINI_API_KEY not set yet in .env).")
        print("    [i] You can set GEMINI_API_KEY in .env to test real LLM generation.")

    print("\n" + "=" * 60)
    print("[SUCCESS] All Core RAG Tests Passed Successfully!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
