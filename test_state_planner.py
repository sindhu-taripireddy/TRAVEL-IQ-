"""
Comprehensive test verifying all 16 Indian states datasets and AI planner endpoints.
"""

import os
import sys
import json

# Ensure UTF-8 output encoding
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from data.states_data import get_all_states, get_state_by_id, STATES_DATA
from planner import generate_state_answer, generate_state_itinerary
from app import app

def test_all_16_states():
    print("=" * 60)
    print("[*] TRAVELIQ Testing All 16 Famous Indian States")
    print("=" * 60)

    states = get_all_states()
    print(f"\n[1] Total Registered States: {len(states)}")
    assert len(states) == 16, f"Expected 16 states, got {len(states)}"

    expected_ids = [
        "andhra_pradesh", "kerala", "goa", "rajasthan", "uttarakhand",
        "kashmir_ladakh", "maharashtra", "gujarat", "uttar_pradesh",
        "west_bengal_sikkim", "karnataka", "tamil_nadu", "himachal_pradesh",
        "madhya_pradesh", "odisha", "meghalaya"
    ]

    for sid in expected_ids:
        st = get_state_by_id(sid)
        print(f"    ✓ [{st['name']}]: {len(st['top_destinations'])} destination hubs, {len(st['authentic_cuisine'])} dishes")
        assert len(st["top_destinations"]) >= 1
        assert len(st["authentic_cuisine"]) >= 3

    print("\n[2] Testing AI Q&A Across Different States")
    # Kashmir test
    ans_kashmir = generate_state_answer("What should I not miss in Gulmarg and Dal Lake?", "kashmir_ladakh")
    print(f"    [OK] Kashmir Answer snippet: {ans_kashmir['answer'][:120]}...")
    assert "Kashmir" in ans_kashmir["state"] or "Ladakh" in ans_kashmir["state"]

    # Meghalaya test
    ans_meg = generate_state_answer("Tell me about living root bridges and Dawki river.", "meghalaya")
    print(f"    [OK] Meghalaya Answer snippet: {ans_meg['answer'][:120]}...")

    # Uttar Pradesh test
    ans_up = generate_state_answer("What is special about Varanasi Ganga Aarti and Awadhi food?", "uttar_pradesh")
    print(f"    [OK] Uttar Pradesh Answer snippet: {ans_up['answer'][:120]}...")

    print("\n[3] Testing Personalized Itinerary Generation for Gujarat (4 Days)")
    plan_guj = generate_state_itinerary("gujarat", 4, "16000", ["Wildlife", "Heritage", "Food"])
    print(f"    [OK] Gujarat Plan generated successfully for {plan_guj['duration']} days.")

    print("\n[4] Testing Flask API: /api/states")
    client = app.test_client()
    resp = client.get("/api/states")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["count"] == 16
    print(f"    [OK] /api/states returned all {data['count']} states.")

    print("\n" + "=" * 60)
    print("[SUCCESS] All 16 Indian States Datasets & Endpoints Verified!")
    print("=" * 60)

if __name__ == "__main__":
    test_all_16_states()
