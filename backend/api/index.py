"""
Vercel Serverless Function Entry Point
This file serves as the entry point for Vercel's serverless function deployment.
"""
import sys
from pathlib import Path

# Add the parent directory to the path so we can import from backend/
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app

# Vercel expects 'app' to be exposed directly
__all__ = ['app']
