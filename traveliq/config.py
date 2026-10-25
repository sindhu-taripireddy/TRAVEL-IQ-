"""
TRAVELIQ — Application Configuration Module
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Base configuration settings."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "traveliq-state-secret-2026")
    GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "").strip()
    PORT = int(os.environ.get("PORT", 5000))
    CORS_HEADERS = "Content-Type"
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False

class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
