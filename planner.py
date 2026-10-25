"""
TRAVELIQ — Planner Compatibility Facade
Re-exports services from traveliq.services for backward compatibility.
"""

from traveliq.services.gemini_service import get_gemini_client, call_gemini_llm, TRAVELIQ_SYSTEM_PROMPT
from traveliq.services.state_service import format_state_context
from traveliq.services.planner_service import (
    generate_state_answer,
    generate_state_itinerary,
    generate_local_state_answer,
    generate_local_itinerary
)
