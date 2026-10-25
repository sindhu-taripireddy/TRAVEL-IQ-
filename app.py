"""
TRAVELIQ — Application Entrypoint
Runs the modular Flask application.
"""

import os
import sys

# Ensure UTF-8 output encoding on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from traveliq import create_app

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print("=" * 60)
    print("[*] TRAVELIQ Server is RUNNING SUCCESSFULLY!")
    print(f"[*] Open this link in your browser: http://127.0.0.1:{port}")
    print("[*] Press CTRL + C in terminal to stop the server")
    print("=" * 60)
    app.run(host="0.0.0.0", port=port, debug=False)
