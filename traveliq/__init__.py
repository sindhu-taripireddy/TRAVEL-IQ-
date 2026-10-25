"""
TRAVELIQ — Application Factory
Initializes Flask, extensions, blueprints, and templates.
"""

import os
from flask import Flask
from flask_cors import CORS
from traveliq.config import Config


def create_app(config_class=Config) -> Flask:
    """Create and configure the Flask application instance."""
    # Base directory for locating templates and static assets
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    template_dir = os.path.join(base_dir, "templates")
    static_dir = os.path.join(base_dir, "static")

    app = Flask(
        __name__,
        template_folder=template_dir,
        static_folder=static_dir,
        static_url_path="/static"
    )

    app.config.from_object(config_class)

    # Enable CORS for all REST API endpoints
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register blueprints
    from traveliq.routes.web import web_bp
    from traveliq.routes.api import api_bp

    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp)

    return app
