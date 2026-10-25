"""
TRAVELIQ — Google Gemini LLM Service
Handles Gemini API integration, model fallback cascades, and content generation.
"""

import os
from typing import Optional

TRAVELIQ_SYSTEM_PROMPT = """You are TRAVELIQ, an expert AI Travel Research Assistant and Smart Trip Planner for Indian States.
MANDATORY GUIDELINES:
1. ALWAYS mention the EXACT LOCATION (city, road, district, area) for every attraction, destination, and restaurant.
2. ALWAYS specify DISTANCES IN KILOMETERS (km) from major transit hubs, railway stations, airports, or between tourist spots.
3. ALWAYS recommend NEARBY FAMOUS FOOD SPOTS with their exact location, distance in km from the attraction, and must-try signature dishes.
4. Provide structured, practical day-by-day itineraries with Morning, Afternoon, and Evening slots, budget estimates, and transport tips."""


def get_gemini_client():
    """Retrieve configured Gemini API client if API key exists."""
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key or api_key == "your_gemini_api_key_here":
        return None

    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        return genai
    except Exception:
        return None


def call_gemini_llm(prompt: str, system_instruction: str = TRAVELIQ_SYSTEM_PROMPT) -> Optional[str]:
    """Execute Gemini prompt with fallback models."""
    genai = get_gemini_client()
    if not genai:
        return None

    models = ["gemini-1.5-flash", "gemini-2.0-flash", "gemini-1.5-pro", "gemini-pro"]
    for model_name in models:
        try:
            if "1.5" in model_name or "2.0" in model_name:
                model = genai.GenerativeModel(
                    model_name=model_name,
                    system_instruction=system_instruction
                )
            else:
                model = genai.GenerativeModel(model_name=model_name)

            response = model.generate_content(
                prompt,
                generation_config={"temperature": 0.3, "top_p": 0.85}
            )

            if response and response.text:
                return response.text
        except Exception as e:
            continue

    return None
