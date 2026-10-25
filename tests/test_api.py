"""
TRAVELIQ — REST API Integration Tests
"""

import json
from traveliq import create_app
from traveliq.config import TestingConfig


def test_api_endpoints():
    """Verify all REST API endpoints."""
    app = create_app(TestingConfig)
    client = app.test_client()

    # 1. GET /
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"TRAVELIQ" in resp.data

    # 2. GET /api/health
    resp = client.get("/api/health")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["status"] == "healthy"
    assert data["total_states"] >= 16

    # 3. GET /api/states
    resp = client.get("/api/states")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["count"] >= 16

    # 4. GET /api/states/andhra_pradesh
    resp = client.get("/api/states/andhra_pradesh")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["state"]["name"] == "Andhra Pradesh"

    # 5. POST /api/chat error handling
    resp = client.post("/api/chat", json={})
    assert resp.status_code == 400

    # 6. POST /api/chat valid query
    resp = client.post("/api/chat", json={
        "question": "What are the best food spots near RK Beach with distances in km?",
        "state_id": "andhra_pradesh"
    })
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["status"] == "success"
    assert len(data["answer"]) > 10

    # 7. POST /api/plan
    resp = client.post("/api/plan", json={
        "state_id": "kerala",
        "duration": 4,
        "budget": "20000",
        "interests": ["Beaches & Lakes", "Authentic Cuisine"]
    })
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert data["status"] == "success"
    assert "DAY 1" in data["plan"] or "Day 1" in data["plan"]

    print("[SUCCESS] All API tests passed!")


if __name__ == "__main__":
    test_api_endpoints()
