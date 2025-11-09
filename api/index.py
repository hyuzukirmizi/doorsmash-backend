"""
Vercel Serverless Function Entry Point (root rewrite)
This exposes the unified FastAPI app defined in backend/main.py
"""
import sys
from pathlib import Path

# Two possible layouts:
# 1. Project root contains backend/ (our repo) -> need backend/ in path then import main
# 2. Vercel root IS backend/ (api folder is sibling inside backend) -> main.py adjacent to api folder

CURRENT_DIR = Path(__file__).resolve().parent
BACKEND_DIR = CURRENT_DIR / "backend"

if BACKEND_DIR.exists() and (BACKEND_DIR / "main.py").exists():
    sys.path.insert(0, str(BACKEND_DIR))
    from main import app
elif (CURRENT_DIR.parent / "backend" / "main.py").exists():
    sys.path.insert(0, str(CURRENT_DIR.parent / "backend"))
    from main import app
elif (CURRENT_DIR / "main.py").exists():
    sys.path.insert(0, str(CURRENT_DIR))
    from main import app
else:
    raise ImportError("main.py not found for FastAPI app. Checked backend/, parent/backend/, and current directory.")

__all__ = ["app"]
