"""
TRAVELIQ — Web View Routes
Renders the client web application and dashboard.
"""

from flask import Blueprint, render_template

web_bp = Blueprint("web", __name__)


@web_bp.route("/", methods=["GET"])
def index():
    """Render the main TravelIQ web dashboard."""
    return render_template("index.html")
