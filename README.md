# ResearchPilot AI - Autonomous Research Intelligence Hub

An AI-powered research assistant that helps researchers discover, organize, and interact with academic papers through intelligent search, summarization, and contextual Q&A.

## Features

✅ **Paper Discovery** - Search academic papers from arXiv
✅ **Smart Organization** - Save and manage your research library
✅ **AI Summarization** - Get concise summaries of complex papers
✅ **Contextual Q&A** - Ask questions about your research papers
✅ **Research Assistance** - AI-powered insights and recommendations

## Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **ChromaDB** - Vector database for semantic search
- **OpenAI API** - LLM for summarization and Q&A
- **arXiv API** - Academic paper discovery

### Frontend
- **React** - Modern UI framework
- **Axios** - HTTP client
- **React Icons** - Icon library

## Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- OpenAI API key

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```bash
copy .env.example .env
```

5. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_actual_api_key_here
CHROMA_PERSIST_DIR=./chroma_db
```

6. Run the backend:
```bash
python main.py
```

Backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm start
```

Frontend will run on `http://localhost:3000`

## Usage

### 1. Search Papers
- Enter keywords in the search bar
- Browse results with titles, authors, and abstracts
- Click "PDF" to view the full paper

### 2. Save Papers
- Click "Save" button on any paper card
- Access saved papers in "My Library" tab

### 3. AI Summarization
- Click "Summarize" on any paper
- Get structured summaries with key findings

### 4. Ask Questions
- Go to "Ask Questions" tab
- Type your research question
- Get AI-powered answers based on your saved papers

## API Endpoints

### Search Papers
```
POST /api/search
Body: { "query": "machine learning", "max_results": 10 }
```

### Summarize Paper
```
POST /api/summarize
Body: { "paper_id": "2301.12345" }
```

### Ask Question
```
POST /api/question
Body: { "question": "What are the main findings?", "paper_id": "optional" }
```

### Save Paper
```
POST /api/papers/save?paper_id=2301.12345
```

### Get Saved Papers
```
GET /api/papers/saved
```

### Delete Paper
```
DELETE /api/papers/{paper_id}
```

## Project Structure

```
Cerebro Nexus/
├── backend/
│   ├── services/
│   │   ├── paper_service.py    # arXiv integration
│   │   ├── vector_service.py   # ChromaDB operations
│   │   └── llm_service.py      # OpenAI integration
│   ├── main.py                 # FastAPI app
│   ├── requirements.txt
│   └── .env
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── SearchBar.js
│   │   │   ├── PaperCard.js
│   │   │   ├── QAPanel.js
│   │   │   └── SavedPapers.js
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   └── package.json
└── README.md
```

## Features in Detail

### Paper Discovery
- Real-time search across arXiv database
- Relevance-based sorting
- Comprehensive metadata (authors, dates, categories)

### Smart Organization
- Vector-based storage for semantic search
- Persistent library across sessions
- Easy management (save/delete)

### AI Summarization
- Structured summaries with:
  - Main objective
  - Key methodology
  - Important findings
  - Significance

### Contextual Q&A
- Ask questions about specific papers or entire library
- Context-aware responses
- Source citations

## Troubleshooting

### Backend Issues
- Ensure OpenAI API key is valid
- Check Python version (3.8+)
- Verify all dependencies are installed

### Frontend Issues
- Clear npm cache: `npm cache clean --force`
- Delete node_modules and reinstall: `rm -rf node_modules && npm install`
- Check if backend is running on port 8000

### CORS Issues
- Ensure backend CORS settings allow `http://localhost:3000`
- Check browser console for specific errors

## Future Enhancements

- [ ] PDF text extraction and analysis
- [ ] Citation network visualization
- [ ] Collaborative research spaces
- [ ] Export to reference managers
- [ ] Advanced filtering and sorting
- [ ] Multi-language support

## License

MIT License

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

## Support

For issues or questions, please open a GitHub issue.
