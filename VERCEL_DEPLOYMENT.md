# 🚀 Vercel Deployment Guide - DoorSmash Backend

## 📋 Overview

This backend is deployed on Vercel and serves APIs for:
- **Orders Management** - Create, track, and manage food orders
- **Nutrition Tracking** - Log meals, track calories and macros
- **AI Chatbot** - Gemini-powered conversational assistant

**Deployed URL:** `https://doorsmash-backend.vercel.app`

---

## ✅ CORS Configuration

The backend is configured to accept requests from:
- ✅ `https://doorsmash-git-main-hyuzukirmizis-projects.vercel.app` (Production)
- ✅ `https://doorsmash-92mnnq0bn-hyuzukirmizis-projects.vercel.app` (Preview)
- ✅ `https://www.udoorsmashorpass.tech` (Custom Domain)
- ✅ `https://*.vercel.app` (All Vercel preview deployments)
- ✅ `http://localhost:5173` (Local development)
- ✅ `http://localhost:3000` (Local development)

**Files updated:**
- `backend/main.py` - Main API CORS
- `backend/chatbot_api.py` - Chatbot API CORS

---

## 🔧 Environment Variables Required

### Required for Vercel Deployment

```bash
# Supabase Configuration
SUPABASE_URL=https://btevtyamuxysdmenjsdi.supabase.co
SUPABASE_KEY=your_supabase_service_role_key_here

# Google Gemini API (for chatbot)
GOOGLE_API_KEY=your_google_gemini_api_key_here

# Frontend URL (for CORS reference)
FRONTEND_URL=https://www.udoorsmashorpass.tech

# API Base URLs (self-referencing for internal calls)
NUTRITION_API_BASE=https://doorsmash-backend.vercel.app
ORDERS_API_BASE=https://doorsmash-backend.vercel.app
```

### How to Set in Vercel

1. Go to: https://vercel.com/hyuzukirmizis-projects/doorsmash-backend
2. Click **Settings** → **Environment Variables**
3. Add each variable above
4. Set scope to: **Production, Preview, and Development**
5. Click **Save**
6. Redeploy the project

---

## 📦 API Endpoints

### Health Check
```bash
GET https://doorsmash-backend.vercel.app/api/health
GET https://doorsmash-backend.vercel.app/health
```

**Response:**
```json
{
  "status": "healthy",
  "services": {
    "orders": "available",
    "nutrition": "available"
  }
}
```

### Orders API
```bash
GET  https://doorsmash-backend.vercel.app/orders
POST https://doorsmash-backend.vercel.app/orders
GET  https://doorsmash-backend.vercel.app/orders/{order_id}
GET  https://doorsmash-backend.vercel.app/users/{user_id}/orders
```

### Nutrition API
```bash
GET  https://doorsmash-backend.vercel.app/api/nutrition/food-items/search
POST https://doorsmash-backend.vercel.app/api/nutrition/meals
GET  https://doorsmash-backend.vercel.app/api/nutrition/profiles/{user_id}
GET  https://doorsmash-backend.vercel.app/api/nutrition/totals/user/{user_id}/today
```

### Chatbot API
```bash
POST https://doorsmash-backend.vercel.app/api/chat
GET  https://doorsmash-backend.vercel.app/history/{user_id}
```

**Chat Request:**
```json
{
  "message": "Show me today's menu",
  "user_id": "uuid-here",
  "user_location": {
    "latitude": 42.3914,
    "longitude": -72.5295
  }
}
```

---

## 🧪 Testing the Deployment

### Quick Test Commands

```bash
# Health check
curl https://doorsmash-backend.vercel.app/api/health

# Orders endpoint
curl https://doorsmash-backend.vercel.app/orders

# Search food items
curl "https://doorsmash-backend.vercel.app/api/nutrition/food-items/search?q=chicken&limit=5"

# Chatbot test
curl -X POST https://doorsmash-backend.vercel.app/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "user_id": "test-user"}'
```

### Browser Console Test

Open your frontend at https://www.udoorsmashorpass.tech and run:

```javascript
// Test backend connectivity
fetch('https://doorsmash-backend.vercel.app/api/health')
  .then(r => r.json())
  .then(console.log);
```

Expected: No CORS errors, status 200

---

## 🔄 Deployment Workflow

### Automatic Deployment

Every `git push` to the `main` branch triggers automatic deployment to Vercel.

```bash
git add .
git commit -m "Update CORS configuration for production"
git push origin main
```

### Manual Deployment

```bash
# Install Vercel CLI if not already installed
npm i -g vercel

# Deploy to production
vercel --prod
```

---

## 📂 Project Structure

```
doorsmash-backend/
├── backend/
│   ├── main.py                  # Main unified API (Orders + Nutrition)
│   ├── chatbot_api.py           # AI Chatbot API
│   ├── orders_api.py            # Orders management
│   ├── nutrition_api.py         # Nutrition tracking
│   ├── nutrition_db.py          # Database operations
│   ├── nutrition_models.py      # Pydantic models
│   ├── requirements.txt         # Python dependencies
│   ├── vercel.json             # Vercel configuration
│   └── api/
│       ├── index.py            # Vercel entry point (main API)
│       └── chat.py             # Vercel entry point (chatbot)
├── VERCEL_DEPLOYMENT.md        # This file
└── README.md
```

---

## ⚠️ Important Notes

### CORS Wildcard Pattern

The pattern `https://*.vercel.app` in the allow_origins list does **NOT** work as a wildcard in Python's CORSMiddleware. Each specific URL must be listed individually.

**Current workaround:** We explicitly list:
- Main production URL
- Preview deployment URL
- Custom domain

For dynamic preview URLs, consider using a CORS library that supports regex patterns or implement custom middleware.

### Environment Variables

- Use **SERVICE ROLE KEY** for `SUPABASE_KEY` (not anon key)
- Frontend uses **ANON KEY** (different from backend)
- Changes to env vars require redeployment to take effect

### API Routes

All API routes must start with `/api/` for proper Vercel routing (configured in `vercel.json`).

---

## 🐛 Troubleshooting

### CORS Errors

**Symptom:** Browser console shows "blocked by CORS policy"

**Solutions:**
1. Verify frontend URL is in the `allow_origins` list
2. Check environment variables are set in Vercel
3. Redeploy after changing CORS config
4. Clear browser cache

### 404 Errors

**Symptom:** API endpoint returns 404

**Solutions:**
1. Check route starts with `/api/` for Vercel
2. Verify `vercel.json` rewrites configuration
3. Check function exists in the correct file

### Environment Variables Not Loading

**Symptom:** "SUPABASE_URL is not set" error

**Solutions:**
1. Check variable names in Vercel dashboard (no typos)
2. Ensure scope is set to "Production"
3. Redeploy after adding variables
4. Check deployment logs for errors

### Logs and Debugging

**View Deployment Logs:**
1. Go to https://vercel.com/hyuzukirmizis-projects/doorsmash-backend
2. Click on the latest deployment
3. Click "View Function Logs"
4. Check for errors or warnings

---

## 📚 Related Documentation

- **Vercel Python Runtime:** https://vercel.com/docs/functions/runtimes/python
- **FastAPI CORS:** https://fastapi.tiangolo.com/tutorial/cors/
- **FastAPI Deployment:** https://fastapi.tiangolo.com/deployment/

---

## 🎯 Frontend Integration

Your frontend should use these environment variables:

```bash
VITE_API_URL=https://doorsmash-backend.vercel.app
VITE_CHATBOT_API_URL=https://doorsmash-backend.vercel.app/api/chat
```

**Frontend repository:** https://github.com/hyuzukirmizi/doorsmash

---

## ✅ Deployment Checklist

Before deploying:

- [x] CORS configured with all frontend URLs
- [x] Environment variables set in Vercel
- [x] `vercel.json` properly configured
- [x] Dependencies listed in `requirements.txt`
- [x] All API routes start with `/api/`
- [ ] Test all endpoints after deployment
- [ ] Verify CORS from frontend
- [ ] Check Vercel logs for errors

---

**Last Updated:** November 9, 2025
**Maintainer:** hyuzukirmizi
**Status:** ✅ Production Ready
