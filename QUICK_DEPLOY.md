# ⚡ Quick Deploy - Backend

## 🚀 Deploy to Vercel

```bash
# From doorsmash-backend directory
git add .
git commit -m "Update CORS for production deployment"
git push origin main
```

Vercel will automatically deploy! ✅

---

## 🔧 Environment Variables to Set

Go to: https://vercel.com/hyuzukirmizis-projects/doorsmash-backend/settings/environment-variables

**Copy and paste these:**

```
SUPABASE_URL=https://btevtyamuxysdmenjsdi.supabase.co
SUPABASE_KEY=your_service_role_key_here
GOOGLE_API_KEY=your_gemini_api_key_here
FRONTEND_URL=https://www.udoorsmashorpass.tech
NUTRITION_API_BASE=https://doorsmash-backend.vercel.app
ORDERS_API_BASE=https://doorsmash-backend.vercel.app
```

> ⚠️ Use **SERVICE ROLE KEY** for SUPABASE_KEY (not anon key)

---

## 🧪 Test After Deploy

```bash
# Health check
curl https://doorsmash-backend.vercel.app/api/health

# Should return:
# {"status": "healthy", "services": {"orders": "available", "nutrition": "available"}}
```

---

## ✅ What Changed

### Files Updated:
- ✅ `backend/main.py` - CORS configuration
- ✅ `backend/chatbot_api.py` - CORS configuration

### CORS Now Allows:
- ✅ https://www.udoorsmashorpass.tech
- ✅ https://doorsmash-git-main-hyuzukirmizis-projects.vercel.app
- ✅ https://doorsmash-92mnnq0bn-hyuzukirmizis-projects.vercel.app
- ✅ All Vercel preview deployments

---

## 🔗 Important URLs

| Service | URL |
|---------|-----|
| **Backend API** | https://doorsmash-backend.vercel.app |
| **Health Check** | https://doorsmash-backend.vercel.app/api/health |
| **API Docs** | https://doorsmash-backend.vercel.app/docs |
| **Orders API** | https://doorsmash-backend.vercel.app/orders |
| **Chatbot API** | https://doorsmash-backend.vercel.app/api/chat |

---

## 📚 Full Documentation

See `VERCEL_DEPLOYMENT.md` for complete deployment guide.
