"""
TRAVELIQ — State Data & Intelligence Service
Handles state lookup, metadata summaries, and structured prompt formatting.
"""

from typing import Dict, Any, List
from data.states_data import STATES_DATA, get_all_states, get_state_by_id


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
