"""
Chatbot API Serverless Function Entry Point
"""
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from backend/
sys.path.append(str(Path(__file__).parent.parent))

from chatbot_api import app

# Expose FastAPI app for Vercel Python runtime
# Vercel detects `app` by default; keep `handler` for backward compatibility
handler = app
__all__ = ["app"]
