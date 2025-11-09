"""
Chatbot API Serverless Function Entry Point
"""
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from backend/
sys.path.append(str(Path(__file__).parent.parent))

from chatbot_api import app, chat as chat_handler

# Add an alias so POST "/" works inside the serverless function environment
# Vercel typically strips the function path and routes requests to "/".
# This makes POST /chat (rewritten to /api/chat) hit the same handler.
app.add_api_route("/", chat_handler, methods=["POST"])

# Expose FastAPI app for Vercel Python runtime
# Vercel detects `app` by default; keep `handler` for backward compatibility
handler = app
__all__ = ["app"]
