"""
TRAVELIQ — Direct State Travel Intelligence & Itinerary Planner
Connects curated state datasets with Google Gemini API, including Exact Locations, Distances in km, and Nearby Food Places.
"""

import os
import sys
from typing import Dict, Any, List, Optional
from dotenv import load_dotenv

# Ensure UTF-8 output encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

load_dotenv()

from data.states_data import STATES_DATA, get_state_by_id, get_all_states

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


def format_state_context(state_info: Dict[str, Any]) -> str:
    """Format structured state data into detailed text context for Gemini with locations, distances, and food spots."""
    lines = [
        f"STATE: {state_info['name']} ({state_info.get('tagline', '')})",
        f"Capital: {state_info.get('capital', 'N/A')}",
        f"Best Time to Visit: {state_info.get('best_time_to_visit', 'Year-round')}",
        f"Ideal Duration: {state_info.get('ideal_duration', '3-7 days')}",
        "",
        "ESTIMATED DAILY BUDGET TIERS:",
        f"- Budget: {state_info['estimated_daily_budget'].get('budget', 'N/A')}",
        f"- Mid-Range: {state_info['estimated_daily_budget'].get('mid_range', 'N/A')}",
        f"- Luxury: {state_info['estimated_daily_budget'].get('luxury', 'N/A')}",
        "",
        "TOP DESTINATIONS & ATTRACTIONS (WITH LOCATIONS, DISTANCES & NEARBY FOOD):"
    ]

    for dest in state_info.get("top_destinations", []):
        lines.append(f"\n* {dest['name']} [{dest.get('category', 'Attraction')}]:")
        lines.append(f"  - Exact Location: {dest.get('exact_location', 'N/A')}")
        lines.append(f"  - Distance & Transit: {dest.get('distance_from_hub', 'N/A')}")
        lines.append("  - Key Highlights:")
        for h in dest.get("highlights", []):
            lines.append(f"    • {h}")

        if "nearby_food_places" in dest and dest["nearby_food_places"]:
            lines.append("  - Nearby Food Places & Restaurants:")
            for f in dest["nearby_food_places"]:
                lines.append(
                    f"    🍲 {f['name']} | Location: {f['location']} | Distance: {f['distance_km']} | Specialty: {f['specialty']}"
                )

    lines.append("\nAUTHENTIC CUISINE & MUST-TRY DISHES:")
    for dish in state_info.get("authentic_cuisine", []):
        lines.append(f"- {dish}")

    lines.append("\nLOCAL TRANSPORT & CONNECTIVITY:")
    for t in state_info.get("local_transport", []):
        lines.append(f"- {t}")

    lines.append("\nTRAVEL RULES, SAFETY & TIPS:")
    for tip in state_info.get("travel_tips_and_rules", []):
        lines.append(f"- {tip}")

    return "\n".join(lines)


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
                return response.text.strip()
        except Exception:
            continue

    return None


def generate_local_state_answer(question: str, state_info: Dict[str, Any]) -> str:
    """Generate state answer with exact locations, distances in km, and nearby food spots when Gemini is offline."""
    q_lower = question.lower()
    name = state_info["name"]

    # If asking about places / attractions / food / distances
    dests = state_info.get("top_destinations", [])
    
    # 1. Food / Restaurant query
    if any(w in q_lower for w in ["food", "restaurant", "eat", "dish", "cuisine", "breakfast", "dinner", "lunch"]):
        res_blocks = []
        for d in dests:
            if "nearby_food_places" in d and d["nearby_food_places"]:
                foods = []
                for f in d["nearby_food_places"]:
                    foods.append(
                        f"  - **{f['name']}**\n"
                        f"    📍 *Location*: {f['location']}\n"
                        f"    🚗 *Distance*: {f['distance_km']}\n"
                        f"    ✨ *Must-Try*: {f['specialty']}"
                    )
                res_blocks.append(f"### 📍 Near {d['name']}:\n" + "\n\n".join(foods))
        
        all_food_str = "\n\n".join(res_blocks)
        cuisine_list = "\n".join([f"• {c}" for c in state_info["authentic_cuisine"][:4]])
        return (
            f"### 🍲 Famous Food Spots & Nearby Restaurants in {name}\n\n"
            f"**State Culinary Specialties:**\n{cuisine_list}\n\n"
            f"---\n\n"
            f"{all_food_str}"
        )

    # 2. Places / Locations / Distances query
    if any(w in q_lower for w in ["place", "visit", "attraction", "location", "distance", "km", "reach", "see"]):
        dests_blocks = []
        for d in dests:
            food_recommendations = ""
            if "nearby_food_places" in d and d["nearby_food_places"]:
                f_items = []
                for f in d["nearby_food_places"]:
                    f_items.append(
                        f"  - 🍲 **{f['name']}** (*{f['distance_km']}* at {f['location']}) — *Specialty*: {f['specialty']}"
                    )
                food_recommendations = "\n**Nearby Food Places:**\n" + "\n".join(f_items)

            highlights_text = "\n  • ".join(d["highlights"][:3])
            dests_blocks.append(
                f"### 📍 {d['name']} *({d.get('category', 'Attraction')})*\n"
                f"📌 **Exact Location**: {d.get('exact_location', 'City Center')}\n"
                f"🚗 **Distance / Transit**: {d.get('distance_from_hub', 'Accessible via main road')}\n"
                f"🌟 **Key Highlights**:\n  • {highlights_text}\n"
                f"{food_recommendations}"
            )

        return (
            f"### 🗺️ Top Places, Exact Locations & Nearby Food in {name}\n\n"
            f"{'---\n\n'.join(dests_blocks)}\n\n"
            f"📅 **Best Season to Visit**: {state_info['best_time_to_visit']}\n"
            f"💰 **Daily Budget**: {state_info['estimated_daily_budget']['mid_range']}"
        )

    # General overview with location and food
    d_first = dests[0] if dests else None
    food_sample = ""
    if d_first and "nearby_food_places" in d_first and d_first["nearby_food_places"]:
        nf = d_first["nearby_food_places"][0]
        food_sample = f"\n• **Nearby Food Spot**: {nf['name']} ({nf['distance_km']} from {d_first['name']}) - *{nf['specialty']}*"

    return (
        f"### ✈️ Travel & Location Guide: {name}\n\n"
        f"**{state_info.get('tagline', '')}**\n\n"
        f"• **Capital / Hub**: {state_info.get('capital', 'Key Hub')}\n"
        f"• **Sample Destination**: {d_first['name'] if d_first else 'Iconic Places'}\n"
        f"• **Exact Location**: {d_first.get('exact_location', 'N/A') if d_first else 'N/A'}\n"
        f"• **Distance in KM**: {d_first.get('distance_from_hub', 'N/A') if d_first else 'N/A'}"
        f"{food_sample}\n"
        f"• **Best Season**: {state_info['best_time_to_visit']}\n"
        f"• **Daily Budget**: {state_info['estimated_daily_budget']['mid_range']}\n\n"
        f"💡 *Ask me about specific attractions, exact locations, distances in km, or nearby famous food spots!*"
    )


def generate_local_itinerary(state_info: Dict[str, Any], duration: int, budget: str, interests: List[str]) -> str:
    """Generate structured day-by-day itinerary template with exact locations, distances in km, and nearby food spots."""
    name = state_info["name"]
    dests = state_info.get("top_destinations", [])
    
    days_content = []
    for day in range(1, duration + 1):
        dest_idx = (day - 1) % len(dests)
        cur_dest = dests[dest_idx]
        
        h = cur_dest.get("highlights", [])
        morn = h[0] if len(h) > 0 else "Sightseeing & exploration"
        aft = h[1] if len(h) > 1 else "Cultural discovery & afternoon tour"
        eve = h[2] if len(h) > 2 else "Sunset views & evening bazaar"

        # Nearby food recommendation
        food_rec = ""
        if "nearby_food_places" in cur_dest and cur_dest["nearby_food_places"]:
            f = cur_dest["nearby_food_places"][0]
            food_rec = f"\n  - 🍲 **Recommended Lunch/Dinner**: **{f['name']}** (*{f['distance_km']}* at {f['location']}) — *Try*: {f['specialty']}"

        days_content.append(f"""### 📅 DAY {day}: {cur_dest['name']} ({cur_dest.get('category', 'Tour')})
- 📍 **Exact Location**: {cur_dest.get('exact_location', 'District Center')}
- 🚗 **Distance / Transit**: {cur_dest.get('distance_from_hub', 'Local road connectivity')}
- 🌅 **Morning**: Visit {morn}.
- ☀️ **Afternoon**: Explore {aft}.{food_rec}
- 🌆 **Evening**: Head to {eve} for leisure, sunset viewpoints, and local market shopping.""")

    itinerary_body = "\n\n---\n\n".join(days_content)
    interests_str = ", ".join(interests) if interests else "Sightseeing, Heritage & Food"

    return f"""# ✈️ {duration}-Day Curated Travel Itinerary for {name}

> **Destination Theme**: {state_info.get('tagline', '')}  
> **Target Interests**: {interests_str} | **Budget Target**: ₹{budget if budget else 'Flexible'}

---

## 🌟 Trip Overview & Route Strategy
This {duration}-day route covers the most celebrated locations in **{name}**, optimized with exact distances in kilometers and authentic nearby culinary dining spots.

---

## 🗺️ Day-by-Day Detailed Plan (with Locations, Distances in KM & Nearby Food)

{itinerary_body}

---

## 💰 Budget Breakdown & Estimates
- **Daily Budget Target**: {state_info['estimated_daily_budget'].get('mid_range', '₹3,500 / day')}
- **Food & Dining**: Budget ₹400 - ₹900/day for authentic local meals at the recommended food spots.
- **Local Commute**: {state_info['local_transport'][0]}

## ⚠️ Important Travel Rules & Tips
- {state_info['travel_tips_and_rules'][0]}
- **Best Season to Visit**: {state_info['best_time_to_visit']}
"""


def generate_state_answer(
    question: str,
    state_id: str,
    conversation_history: Optional[List[Dict[str, str]]] = None,
    preferences: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Generate state-grounded answer with exact locations, distances in km, and nearby food places."""
    state_info = get_state_by_id(state_id)
    context_str = format_state_context(state_info)

    history_str = ""
    if conversation_history:
        history_items = []
        for msg in conversation_history[-4:]:
            role = "User" if msg.get("role") == "user" else "Assistant"
            history_items.append(f"{role}: {msg.get('content', '')}")
        if history_items:
            history_str = "Recent Conversation History:\n" + "\n".join(history_items) + "\n\n"

    pref_str = ""
    if preferences:
        parts = []
        if preferences.get("duration"):
            parts.append(f"Duration: {preferences['duration']} days")
        if preferences.get("budget"):
            parts.append(f"Budget: ₹{preferences['budget']}")
        if preferences.get("interests"):
            parts.append(f"Interests: {preferences['interests']}")
        if parts:
            pref_str = "User Preferences:\n" + "\n".join(parts) + "\n\n"

    prompt = f"""{history_str}{pref_str}OFFICIAL STATE TRAVEL KNOWLEDGE BASE (WITH LOCATIONS, DISTANCES IN KM & FOOD PLACES):
{context_str}

USER QUESTION:
{question}

MANDATORY INSTRUCTIONS:
1. When mentioning any place, attraction, or restaurant, ALWAYS state its EXACT LOCATION (road, area, city).
2. ALWAYS include the DISTANCE IN KILOMETERS (km) from key transit hubs, railway stations, airports, or between attractions.
3. ALWAYS provide NEARBY FAMOUS FOOD SPOTS with their exact location, distance in km from the attraction, and must-try specialty dishes.
4. Format output cleanly using markdown with bold headings and bullet points.
"""

    gemini_response = call_gemini_llm(prompt)
    if gemini_response:
        answer_text = gemini_response
        engine = "Google Gemini AI (Grounded in State Locations & Distances)"
    else:
        answer_text = generate_local_state_answer(question, state_info)
        engine = "TRAVELIQ State Location & Food Intelligence"

    return {
        "answer": answer_text,
        "state": state_info["name"],
        "engine": engine,
        "highlights": [d["name"] for d in state_info["top_destinations"][:4]]
    }


def generate_state_itinerary(
    state_id: str,
    duration: int,
    budget: Optional[str],
    interests: List[str],
    preferences: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    """Generate day-by-day itinerary with exact locations, distances in km, and nearby food spots."""
    state_info = get_state_by_id(state_id)
    context_str = format_state_context(state_info)
    interests_str = ", ".join(interests) if interests else "Sightseeing, Culture & Food"
    budget_str = f"₹{budget}" if budget else "Flexible"

    prompt = f"""You are TRAVELIQ, creating a personalized travel plan.

STATE: {state_info['name']}
DURATION: {duration} Days
BUDGET: {budget_str}
USER INTERESTS: {interests_str}

OFFICIAL STATE TRAVEL KNOWLEDGE BASE:
{context_str}

REQUIRED OUTPUT FORMAT (Markdown):
# ✈️ {duration}-Day Curated Travel Itinerary for {state_info['name']}

## 🌟 Trip Highlights & Route Strategy
(Brief overview of route and attractions)

## 🗺️ Day-by-Day Detailed Plan
### DAY 1: [Destination / Hub]
- 📍 **Exact Location**: [Mention exact city, road, or area]
- 🚗 **Distance in KM**: [Distance in km from nearest railway station / airport or transit]
- 🌅 **Morning**: [Attractions & morning activities]
- ☀️ **Afternoon & Nearby Food**: [Afternoon sightseeing + Specific Nearby Restaurant Name with its exact location, distance in km, and signature dish]
- 🌆 **Evening**: [Sunset viewpoints, evening markets & dinner spot with distance in km]

(Repeat for DAY 2 through DAY {duration})

## 🍲 Must-Try Culinary Spots & Food Locations
(List top 3-4 recommended restaurants with exact location, distance in km, and must-try dish)

## 💰 Budget Breakdown & Daily Estimates
(Accommodation, food, local transport, and tickets)

## 🚗 Local Transit & Logistics Guide
(Buses, trains, taxis, and distance guidelines)

## ⚠️ Essential Travel Rules & Tips
(Dress codes, temple timings, safety rules, and season tips)
"""

    gemini_response = call_gemini_llm(prompt)
    if gemini_response:
        plan_text = gemini_response
        engine = "Google Gemini AI (Personalized Itinerary with Locations & KM)"
    else:
        plan_text = generate_local_itinerary(state_info, duration, budget, interests)
        engine = "TRAVELIQ State Location & Food Intelligence"

    return {
        "plan": plan_text,
        "state": state_info["name"],
        "duration": duration,
        "budget": budget,
        "interests": interests,
        "engine": engine
    }
