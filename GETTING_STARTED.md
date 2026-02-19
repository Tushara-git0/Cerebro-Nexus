# 🚀 Getting Started with ResearchPilot AI

## Welcome to ResearchPilot AI!

This guide will help you get your autonomous research intelligence hub up and running in minutes.

---

## 📋 Prerequisites Checklist

Before you begin, make sure you have:

- [ ] **Python 3.8 or higher** installed
  - Check: Open terminal and run `python --version`
  - Download: https://www.python.org/downloads/

- [ ] **Node.js 16 or higher** installed
  - Check: Open terminal and run `node --version`
  - Download: https://nodejs.org/

- [ ] **OpenAI API Key**
  - Get one at: https://platform.openai.com/api-keys
  - You'll need this for AI features

- [ ] **Internet Connection**
  - Required for downloading dependencies and accessing APIs

---

## 🎯 Installation Steps

### Step 1: Run Automated Setup

1. Navigate to the project folder:
   ```
   Cerebro Nexus/
   ```

2. Double-click on `setup.bat`

3. Wait for the installation to complete (this may take 5-10 minutes)

4. You should see:
   ```
   ========================================
   Setup Complete!
   ========================================
   ```

### Step 2: Configure OpenAI API Key

1. Open the file: `backend\.env`

2. You'll see:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   CHROMA_PERSIST_DIR=./chroma_db
   ```

3. Replace `your_openai_api_key_here` with your actual OpenAI API key:
   ```
   OPENAI_API_KEY=sk-proj-abc123xyz...
   CHROMA_PERSIST_DIR=./chroma_db
   ```

4. Save the file

### Step 3: Start the Backend

1. Double-click on `start_backend.bat`

2. A terminal window will open

3. Wait until you see:
   ```
   INFO:     Uvicorn running on http://0.0.0.0:8000
   INFO:     Application startup complete.
   ```

4. **Keep this terminal window open!**

### Step 4: Start the Frontend

1. Double-click on `start_frontend.bat`

2. A new terminal window will open

3. Wait until you see:
   ```
   Compiled successfully!
   
   You can now view researchpilot-frontend in the browser.
   
   Local: http://localhost:3000
   ```

4. Your browser should automatically open to `http://localhost:3000`

5. **Keep this terminal window open too!**

---

## 🎉 You're Ready!

You should now see the ResearchPilot AI interface in your browser.

---

## 🧪 Test Your Installation

### Test 1: Search for Papers

1. In the search bar, type: `machine learning`
2. Click the "Search" button
3. You should see a list of research papers appear

✅ **Success:** Papers are displayed
❌ **Problem:** See troubleshooting section below

### Test 2: Summarize a Paper

1. Find any paper in the search results
2. Click the "Summarize" button
3. Wait a few seconds
4. An AI-generated summary should appear

✅ **Success:** Summary is displayed
❌ **Problem:** Check your OpenAI API key

### Test 3: Save a Paper

1. Click the "Save" button on any paper
2. You should see: "Paper saved successfully!"
3. Click on the "My Library" tab
4. Your saved paper should appear

✅ **Success:** Paper appears in library
❌ **Problem:** Check backend terminal for errors

### Test 4: Ask a Question

1. Click on the "Ask Questions" tab
2. Type a question like: "What are the latest trends in AI?"
3. Click "Ask"
4. Wait for the AI response

✅ **Success:** Answer is displayed
❌ **Problem:** Make sure you have saved papers first

---

## 🎨 User Interface Guide

### Main Navigation Tabs

```
┌─────────────────────────────────────────────────────┐
│  [Search & Discover] [My Library] [Ask Questions]   │
└─────────────────────────────────────────────────────┘
```

### Search & Discover Tab

**What you'll see:**
- Search bar at the top
- Grid of paper cards below
- Each card shows:
  - Paper title
  - Authors
  - Publication date
  - Abstract
  - Action buttons (Save, Summarize, PDF)

**What you can do:**
- Search for papers by keywords
- Read paper abstracts
- Generate AI summaries
- Save papers to your library
- Open PDF versions

### My Library Tab

**What you'll see:**
- List of all your saved papers
- Paper information (title, authors, date)
- Action buttons (View PDF, Delete)

**What you can do:**
- View all saved papers
- Access PDFs quickly
- Remove papers from library

### Ask Questions Tab

**What you'll see:**
- Text area for your question
- "Ask" button
- Answer display area

**What you can do:**
- Ask questions about your research
- Get AI-powered answers
- See source citations

---

## 💡 Usage Tips

### Best Practices

1. **Search Tips:**
   - Use specific keywords: "neural networks" instead of "AI"
   - Try different phrasings if you don't find what you need
   - Use technical terms for better results

2. **Summarization Tips:**
   - Summaries work best on papers you've saved
   - Wait for the full summary to load
   - Summaries include: objective, methodology, findings, significance

3. **Q&A Tips:**
   - Save relevant papers first for better answers
   - Ask specific questions
   - Questions work best when you have 3+ saved papers

4. **Library Management:**
   - Save papers you want to reference later
   - Delete papers you no longer need
   - Keep your library organized

---

## 🔧 Troubleshooting

### Problem: Backend won't start

**Symptoms:**
- Error messages in backend terminal
- "Module not found" errors

**Solutions:**
1. Make sure Python 3.8+ is installed
2. Run setup.bat again
3. Manually activate virtual environment:
   ```bash
   cd backend
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

### Problem: Frontend won't start

**Symptoms:**
- Error messages in frontend terminal
- "npm" not recognized

**Solutions:**
1. Make sure Node.js 16+ is installed
2. Run setup.bat again
3. Manually install dependencies:
   ```bash
   cd frontend
   npm install
   ```

### Problem: "OpenAI API key not found"

**Symptoms:**
- Summarization doesn't work
- Q&A doesn't work
- Error message about API key

**Solutions:**
1. Check that `backend\.env` file exists
2. Verify your API key is correct
3. Make sure there are no extra spaces
4. Restart the backend

### Problem: Search returns no results

**Symptoms:**
- Search completes but shows no papers
- "No results found" message

**Solutions:**
1. Try different search terms
2. Check your internet connection
3. arXiv API might be temporarily down
4. Try again in a few minutes

### Problem: Can't save papers

**Symptoms:**
- "Save" button doesn't work
- Error message when saving

**Solutions:**
1. Check backend terminal for errors
2. Make sure ChromaDB is working
3. Try restarting the backend
4. Delete `chroma_db` folder and restart

### Problem: Browser doesn't open automatically

**Solution:**
- Manually open your browser
- Go to: `http://localhost:3000`

---

## 🛑 Stopping the Application

### To stop the application:

1. **Stop Frontend:**
   - Go to the frontend terminal window
   - Press `Ctrl + C`
   - Type `Y` and press Enter

2. **Stop Backend:**
   - Go to the backend terminal window
   - Press `Ctrl + C`
   - Type `Y` and press Enter

### To restart:
- Just run `start_backend.bat` and `start_frontend.bat` again

---

## 📚 Next Steps

Now that you're up and running:

1. **Explore Features:**
   - Try different search queries
   - Experiment with AI summaries
   - Build your research library

2. **Customize:**
   - Modify the UI in `frontend/src/App.css`
   - Adjust search parameters in `backend/services/paper_service.py`

3. **Learn More:**
   - Read `ARCHITECTURE.md` for technical details
   - Check `README.md` for feature documentation
   - Review `SETUP_GUIDE.md` for advanced configuration

4. **Contribute:**
   - Report bugs
   - Suggest features
   - Share your experience

---

## 🆘 Need Help?

### Resources:
- **README.md** - Feature overview
- **SETUP_GUIDE.md** - Detailed setup instructions
- **ARCHITECTURE.md** - Technical documentation
- **PROJECT_SUMMARY.md** - Quick reference

### Common Questions:

**Q: How much does OpenAI API cost?**
A: OpenAI charges per token. Typical usage costs $0.01-0.10 per session. Check: https://openai.com/pricing

**Q: Can I use a different AI model?**
A: Yes! Edit `backend/services/llm_service.py` and change the model name.

**Q: Can I search other databases besides arXiv?**
A: Yes! You can extend `paper_service.py` to include other sources.

**Q: Is my data private?**
A: Yes! Everything is stored locally except API calls to OpenAI and arXiv.

**Q: Can I deploy this online?**
A: Yes! See SETUP_GUIDE.md for deployment instructions.

---

## ✨ Enjoy Your Research!

You're all set to supercharge your research workflow with AI!

**Happy Researching! 🔬📚🚀**

---

**Quick Reference:**

| Action | Command |
|--------|---------|
| Setup | `setup.bat` |
| Start Backend | `start_backend.bat` |
| Start Frontend | `start_frontend.bat` |
| Backend URL | http://localhost:8000 |
| Frontend URL | http://localhost:3000 |
| Stop | `Ctrl + C` in terminal |

---

**Version:** 1.0.0  
**Last Updated:** 2024
