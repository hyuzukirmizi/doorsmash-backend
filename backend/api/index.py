"""
Vercel Serverless Function Entry Point
This file serves as the entry point for Vercel's serverless function deployment.
It imports the main FastAPI app and exposes it as the handler.
"""
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from backend/
sys.path.append(str(Path(__file__).parent.parent))

from main import app

# Vercel expects the app to be named 'app' or a handler function
handler = app
