"""
TRAVELIQ — Planner & State Data Service Tests
"""

from data.states_data import get_all_states, get_state_by_id
from traveliq.services.planner_service import generate_state_answer, generate_state_itinerary


def test_state_planner():
    """Verify all 16 states data and planner services."""
    states = get_all_states()
    assert len(states) == 16

    # Test Q&A with Andhra Pradesh
    ans = generate_state_answer("Where to eat in Visakhapatnam?", "andhra_pradesh")
    assert ans["state"] == "Andhra Pradesh"
    assert len(ans["answer"]) > 20

    # Test Itinerary for Goa
    plan = generate_state_itinerary("goa", 3, "15000", ["Beaches & Lakes"])
    assert plan["state"] == "Goa"
    assert plan["duration"] == 3
    assert len(plan["plan"]) > 50

    print("[SUCCESS] All Planner Service tests passed!")


if __name__ == "__main__":
    test_state_planner()
