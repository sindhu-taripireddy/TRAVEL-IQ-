"""
Backward-compatibility test runner for Flask endpoints.
"""

from tests.test_api import test_api_endpoints

def test_flask_apis():
    test_api_endpoints()

if __name__ == "__main__":
    test_flask_apis()
