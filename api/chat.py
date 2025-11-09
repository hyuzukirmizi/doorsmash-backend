"""
Vercel Serverless Function Entry Point for Chatbot
This exposes the chatbot FastAPI app defined in backend/chatbot_api.py
"""
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = CURRENT_DIR / "backend"

if BACKEND_DIR.exists() and (BACKEND_DIR / "chatbot_api.py").exists():
    sys.path.insert(0, str(BACKEND_DIR))
    from chatbot_api import app
elif (CURRENT_DIR.parent / "backend" / "chatbot_api.py").exists():
    sys.path.insert(0, str(CURRENT_DIR.parent / "backend"))
    from chatbot_api import app
elif (CURRENT_DIR / "chatbot_api.py").exists():
    sys.path.insert(0, str(CURRENT_DIR))
    from chatbot_api import app
else:
    raise ImportError("chatbot_api.py not found for FastAPI app.")

__all__ = ["app"]
