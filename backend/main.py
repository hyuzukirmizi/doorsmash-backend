"""
Main API - Unified FastAPI Service
Combines Orders API and Nutrition API into a single service
Run this to start both APIs together on port 8000
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

# Import the individual API apps
from orders_api import app as orders_app
from nutrition_api import app as nutrition_app
from chatbot_api import app as chatbot_app

# Create main app
app = FastAPI(
    title="StudentEats API",
    description="Complete API for food ordering and nutrition tracking",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "message": "StudentEats API",
        "version": "1.0.0",
        "services": {
            "orders": {
                "description": "Food ordering and delivery management",
                "endpoints": ["/orders", "/users/{user_id}/orders"]
            },
            "nutrition": {
                "description": "Nutrition tracking and meal logging",
                "endpoints": "/api/nutrition"
            }
        },
        "docs": "/docs"
    }


@app.get("/favicon.ico", include_in_schema=False)
@app.get("/favicon.png", include_in_schema=False)
async def favicon():
    """Return 204 No Content for favicon requests to avoid 404 errors"""
    from fastapi.responses import Response
    return Response(status_code=204)


@app.get("/health")
async def health_check():
    """Health check for the entire API"""
    return {
        "status": "healthy",
        "services": {
            "orders": "available",
            "nutrition": "available"
        }
    }


# Manually add all routes from both apps to avoid mount() issues
# This preserves the original route handlers with all dependencies intact
for route in orders_app.routes:
    if hasattr(route, 'path') and route.path not in ["/"]:
        app.routes.append(route)

for route in nutrition_app.routes:
    if hasattr(route, 'path') and route.path not in ["/", "/health"]:
        app.routes.append(route)

# Fallback: include chatbot routes (/chat, /history/{user_id}) directly so 404s disappear
# Skip its root '/' since we already define one here.
for route in chatbot_app.routes:
    if hasattr(route, 'path') and route.path not in ["/"]:
        # Prevent duplicate insertion if route already present
        if not any(getattr(r, 'path', None) == route.path for r in app.routes):
            app.routes.append(route)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
