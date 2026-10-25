"""
TRAVELIQ — REST API Endpoints
Provides system health, state directory, AI chat, and itinerary generation endpoints.
"""

import os
from flask import Blueprint, request, jsonify
from data.states_data import get_all_states, get_state_by_id, STATES_DATA
from traveliq.services.planner_service import generate_state_answer, generate_state_itinerary

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/health", methods=["GET"])
def health_check():
    """System health check endpoint."""
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    gemini_ready = bool(api_key and api_key != "your_gemini_api_key_here")

    return jsonify({
        "status": "healthy",
        "gemini_configured": gemini_ready,
        "total_states": len(STATES_DATA),
        "supported_states": [s["name"] for s in STATES_DATA.values()]
    }), 200


@api_bp.route("/states", methods=["GET"])
def list_states():
    """Return all available states with metadata."""
    try:
        states = get_all_states()
        return jsonify({
            "status": "success",
            "count": len(states),
            "states": states
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Failed to retrieve states: {str(e)}"
        }), 500


@api_bp.route("/states/<state_id>", methods=["GET"])
def get_state(state_id):
    """Return full detailed travel dataset for a given state."""
    try:
        state_data = get_state_by_id(state_id)
        return jsonify({
            "status": "success",
            "state": state_data
        }), 200
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"State not found: {str(e)}"
        }), 404


@api_bp.route("/chat", methods=["POST", "OPTIONS"])
def chat():
    """AI Travel Research conversational endpoint for states."""
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"status": "error", "message": "Invalid request payload."}), 400

        question = data.get("question", "").strip()
        if not question:
            return jsonify({"status": "error", "message": "Question cannot be empty."}), 400

        state_id = data.get("state_id", "andhra_pradesh")
        history = data.get("history", [])
        preferences = data.get("preferences", {})

        result = generate_state_answer(
            question=question,
            state_id=state_id,
            conversation_history=history,
            preferences=preferences
        )

        return jsonify({
            "status": "success",
            "answer": result["answer"],
            "state": result["state"],
            "engine": result["engine"],
            "highlights": result["highlights"]
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Chat processing failed: {str(e)}"
        }), 500


@api_bp.route("/plan", methods=["POST", "OPTIONS"])
def plan_trip():
    """Generate personalized day-by-day travel plan for a state."""
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200

    try:
        data = request.get_json(silent=True)
        if not data:
            return jsonify({"status": "error", "message": "Invalid request payload."}), 400

        state_id = data.get("state_id", "andhra_pradesh")
        duration = int(data.get("duration", 3))
        if duration < 1 or duration > 30:
            duration = max(1, min(duration, 30))

        budget = str(data.get("budget", "")).strip()
        interests = data.get("interests", [])
        if isinstance(interests, str):
            interests = [i.strip() for i in interests.split(",") if i.strip()]

        result = generate_state_itinerary(
            state_id=state_id,
            duration=duration,
            budget=budget,
            interests=interests
        )

        return jsonify({
            "status": "success",
            "plan": result["plan"],
            "state": result["state"],
            "duration": result["duration"],
            "budget": result["budget"],
            "interests": result["interests"],
            "engine": result["engine"]
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Trip planner failed: {str(e)}"
        }), 500
