"""
Integration test for Flask REST API endpoints in app.py.
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

from app import app

def test_flask_apis():
    print("=" * 60)
    print("[*] Testing Flask REST APIs & Integration")
    print("=" * 60)

    client = app.test_client()

    # 1. Test GET /
    print("\n[1] Testing GET / (Main UI page)")
    resp = client.get("/")
    assert resp.status_code == 200, f"Expected 200, got {resp.status_code}"
    assert b"TRAVELIQ" in resp.data
    print("    [OK] Index HTML served successfully.")

    # 2. Test GET /api/health
    print("\n[2] Testing GET /api/health")
    resp = client.get("/api/health")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    print(f"    [OK] Health Response: status={data.get('status')}, gemini_configured={data.get('gemini_configured')}")
    assert data["status"] == "healthy"

    # 3. Test GET /api/states
    print("\n[3] Testing GET /api/states")
    resp = client.get("/api/states")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    print(f"    [OK] States count: {data.get('count')}")
    assert data["count"] >= 16

    # 4. Test GET /api/states/andhra_pradesh
    print("\n[4] Testing GET /api/states/andhra_pradesh")
    resp = client.get("/api/states/andhra_pradesh")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    print(f"    [OK] State fetched: {data['state']['name']}")

    # 5. Test Error Handling: Empty Question on /api/chat
    print("\n[5] Testing Error Handling: Empty Question on /api/chat")
    resp = client.post("/api/chat", json={"question": ""})
    assert resp.status_code == 400
    print("    [OK] Handled empty question with HTTP 400.")

    # 6. Test /api/chat with valid query
    print("\n[6] Testing POST /api/chat")
    resp = client.post("/api/chat", json={
        "question": "What historic places can I visit in Visakhapatnam?",
        "state_id": "andhra_pradesh"
    })
    data = json.loads(resp.data)
    print(f"    [OK] Chat Response status_code={resp.status_code}, status={data.get('status')}")
    assert resp.status_code == 200
    assert data.get("status") == "success"

    # 7. Test /api/plan
    print("\n[7] Testing POST /api/plan")
    resp = client.post("/api/plan", json={
        "state_id": "kerala",
        "duration": 4,
        "budget": "15000",
        "interests": ["Backwaters", "Food", "Hills"]
    })
    data = json.loads(resp.data)
    print(f"    [OK] Plan Response status_code={resp.status_code}, status={data.get('status')}")
    assert resp.status_code == 200
    assert data.get("status") == "success"

    print("\n" + "=" * 60)
    print("[SUCCESS] All API Endpoint Tests Completed Successfully!")
    print("=" * 60)

if __name__ == "__main__":
    test_flask_apis()
