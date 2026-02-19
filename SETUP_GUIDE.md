# ResearchPilot AI - Setup & Configuration Guide

## Quick Start (Windows)

### Option 1: Automated Setup
1. Double-click `setup.bat`
2. Wait for installation to complete
3. Edit `backend\.env` and add your OpenAI API key
4. Run `start_backend.bat` in one terminal
5. Run `start_frontend.bat` in another terminal
6. Open browser to `http://localhost:3000`

### Option 2: Manual Setup

#### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# Edit .env and add your OpenAI API key
python main.py
```

#### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## Getting OpenAI API Key

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create new secret key
5. Copy the key and paste it in `backend\.env`

```
OPENAI_API_KEY=sk-your-actual-key-here
```

## Configuration Options

### Backend Configuration (backend/.env)

```env
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
CHROMA_PERSIST_DIR=./chroma_db  # Vector database storage location
```

### Frontend Configuration

To change the backend URL, edit `frontend/src/services/api.js`:

```javascript
const API_BASE_URL = 'http://localhost:8000/api';
```

## Testing the Application

### 1. Test Backend
Open browser to `http://localhost:8000`
You should see: `{"message": "ResearchPilot AI - Autonomous Research Intelligence Hub"}`

### 2. Test Frontend
Open browser to `http://localhost:3000`
You should see the ResearchPilot AI interface

### 3. Test Search
- Enter "machine learning" in search bar
- Click Search
- Papers should appear

### 4. Test Summarization
- Click "Summarize" on any paper
- Wait for AI summary to appear

### 5. Test Q&A
- Go to "Ask Questions" tab
- Type a question
- Get AI-powered answer

## Common Issues & Solutions

### Issue: "Module not found" error in backend
**Solution:** Activate virtual environment and reinstall dependencies
```bash
cd backend
venv\Scripts\activate
pip install -r requirements.txt
```

### Issue: "OpenAI API key not found"
**Solution:** Ensure .env file exists and contains valid API key
```bash
cd backend
type .env  # Check if file exists and has correct format
```

### Issue: Frontend can't connect to backend
**Solution:** 
1. Ensure backend is running on port 8000
2. Check CORS settings in `backend/main.py`
3. Verify API_BASE_URL in `frontend/src/services/api.js`

### Issue: ChromaDB errors
**Solution:** Delete and recreate the database
```bash
cd backend
rmdir /s chroma_db
# Restart backend - it will create new database
```

### Issue: npm install fails
**Solution:**
```bash
cd frontend
npm cache clean --force
rmdir /s node_modules
npm install
```

## Performance Optimization

### Backend
- Use faster embedding models for ChromaDB
- Implement caching for frequent queries
- Add rate limiting for API calls

### Frontend
- Enable React production build: `npm run build`
- Implement pagination for search results
- Add loading skeletons for better UX

## Security Best Practices

1. **Never commit .env file** - It contains your API key
2. **Use environment variables** - Don't hardcode secrets
3. **Implement rate limiting** - Prevent API abuse
4. **Validate user inputs** - Sanitize all inputs
5. **Use HTTPS in production** - Encrypt data in transit

## Deployment

### Backend Deployment (Example: Heroku)
```bash
# Add Procfile
echo "web: uvicorn main:app --host 0.0.0.0 --port $PORT" > Procfile

# Deploy
git init
heroku create researchpilot-api
git add .
git commit -m "Initial commit"
git push heroku main
```

### Frontend Deployment (Example: Vercel)
```bash
cd frontend
npm run build
# Deploy to Vercel
vercel --prod
```

## API Rate Limits

### OpenAI API
- Free tier: Limited requests per minute
- Paid tier: Higher limits based on plan
- Monitor usage at https://platform.openai.com/usage

### arXiv API
- Rate limit: 1 request per 3 seconds
- Bulk downloads: Use API responsibly

## Database Management

### Backup ChromaDB
```bash
cd backend
xcopy chroma_db chroma_db_backup /E /I
```

### Reset Database
```bash
cd backend
rmdir /s chroma_db
# Restart backend to create fresh database
```

## Monitoring & Logging

Add logging to backend services:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Processing request...")
```

## Support & Resources

- **OpenAI Documentation:** https://platform.openai.com/docs
- **FastAPI Documentation:** https://fastapi.tiangolo.com/
- **React Documentation:** https://react.dev/
- **ChromaDB Documentation:** https://docs.trychroma.com/

## Troubleshooting Checklist

- [ ] Python 3.8+ installed
- [ ] Node.js 16+ installed
- [ ] Virtual environment activated
- [ ] All dependencies installed
- [ ] .env file created with valid API key
- [ ] Backend running on port 8000
- [ ] Frontend running on port 3000
- [ ] No firewall blocking ports
- [ ] Internet connection active

## Next Steps

1. Customize the UI in `frontend/src/App.css`
2. Add more AI features in `backend/services/llm_service.py`
3. Implement user authentication
4. Add more data sources beyond arXiv
5. Create mobile-responsive design
6. Add export functionality (PDF, BibTeX)

Happy Researching! 🔬
