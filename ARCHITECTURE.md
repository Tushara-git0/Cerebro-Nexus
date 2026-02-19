# ResearchPilot AI - Architecture Overview

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend (React)                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │  Search  │  │  Library │  │    Q&A   │  │  Paper   │   │
│  │   Bar    │  │   View   │  │   Panel  │  │   Card   │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                         ↓                                    │
│                   API Service (Axios)                        │
└─────────────────────────────────────────────────────────────┘
                            ↓ HTTP/REST
┌─────────────────────────────────────────────────────────────┐
│                      Backend (FastAPI)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │                   API Endpoints                       │  │
│  │  /search  /summarize  /question  /papers/*           │  │
│  └──────────────────────────────────────────────────────┘  │
│                            ↓                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │    Paper     │  │    Vector    │  │     LLM      │     │
│  │   Service    │  │   Service    │  │   Service    │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└─────────────────────────────────────────────────────────────┘
         ↓                    ↓                    ↓
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  arXiv API   │    │  ChromaDB    │    │  OpenAI API  │
│  (Papers)    │    │  (Vectors)   │    │  (GPT-3.5)   │
└──────────────┘    └──────────────┘    └──────────────┘
```

## Component Details

### Frontend Layer

#### 1. SearchBar Component
- **Purpose:** User input for paper search
- **Features:** Real-time search, loading states
- **Props:** onSearch, loading

#### 2. PaperCard Component
- **Purpose:** Display individual paper information
- **Features:** Save, summarize, PDF link
- **Props:** paper, onSave, onSummarize

#### 3. QAPanel Component
- **Purpose:** Question-answering interface
- **Features:** Context-aware Q&A, source citations
- **Props:** onAsk

#### 4. SavedPapers Component
- **Purpose:** Display user's research library
- **Features:** List view, delete functionality
- **Props:** papers, onDelete, onRefresh

#### 5. API Service
- **Purpose:** Centralized API communication
- **Methods:** searchPapers, summarizePaper, askQuestion, savePaper, getSavedPapers, deletePaper

### Backend Layer

#### 1. Main Application (main.py)
- **Framework:** FastAPI
- **Features:** CORS, routing, error handling
- **Endpoints:** 8 REST endpoints

#### 2. Paper Service
- **Purpose:** Academic paper discovery
- **Integration:** arXiv API
- **Methods:**
  - `search_papers()` - Search by query
  - `get_paper()` - Fetch specific paper

#### 3. Vector Service
- **Purpose:** Semantic search and storage
- **Integration:** ChromaDB
- **Methods:**
  - `store_paper()` - Save paper embeddings
  - `get_relevant_context()` - Semantic search
  - `search_all()` - Global search
  - `get_all_papers()` - List saved papers
  - `delete_paper()` - Remove paper

#### 4. LLM Service
- **Purpose:** AI-powered analysis
- **Integration:** OpenAI GPT-3.5
- **Methods:**
  - `summarize()` - Generate paper summaries
  - `answer_question()` - Context-aware Q&A

## Data Flow

### 1. Paper Search Flow
```
User Input → SearchBar → API Service → FastAPI → Paper Service → arXiv API
                                                                      ↓
User Display ← PaperCard ← React State ← API Response ← FastAPI ← Results
```

### 2. Paper Save Flow
```
User Click → PaperCard → API Service → FastAPI → Vector Service → ChromaDB
                                                                      ↓
                                                              Store Embeddings
```

### 3. Summarization Flow
```
User Click → PaperCard → API Service → FastAPI → LLM Service → OpenAI API
                                                                    ↓
User Display ← PaperCard ← React State ← API Response ← FastAPI ← Summary
```

### 4. Q&A Flow
```
User Question → QAPanel → API Service → FastAPI → Vector Service → ChromaDB
                                                        ↓              ↓
                                                   Get Context    Retrieve
                                                        ↓              ↓
                                                   LLM Service ← Relevant Papers
                                                        ↓
                                                   OpenAI API
                                                        ↓
User Display ← QAPanel ← React State ← API Response ← Answer
```

## Technology Stack Details

### Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| React | 18.2.0 | UI framework |
| Axios | 1.6.0 | HTTP client |
| React Icons | 4.11.0 | Icon library |
| React Scripts | 5.0.1 | Build tools |

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| FastAPI | 0.104.1 | Web framework |
| Uvicorn | 0.24.0 | ASGI server |
| OpenAI | 1.3.0 | LLM integration |
| ChromaDB | 0.4.18 | Vector database |
| LangChain | 0.0.335 | LLM orchestration |
| arXiv | 2.1.0 | Paper discovery |
| Pydantic | 2.5.0 | Data validation |

## API Endpoints

### POST /api/search
**Purpose:** Search academic papers
**Request:**
```json
{
  "query": "machine learning",
  "max_results": 10
}
```
**Response:**
```json
{
  "papers": [
    {
      "id": "2301.12345",
      "title": "Paper Title",
      "authors": ["Author 1", "Author 2"],
      "summary": "Abstract...",
      "published": "2023-01-15T00:00:00",
      "pdf_url": "https://arxiv.org/pdf/2301.12345",
      "categories": ["cs.LG"]
    }
  ]
}
```

### POST /api/summarize
**Purpose:** Generate AI summary of paper
**Request:**
```json
{
  "paper_id": "2301.12345"
}
```
**Response:**
```json
{
  "summary": "Structured summary with key points..."
}
```

### POST /api/question
**Purpose:** Answer questions about papers
**Request:**
```json
{
  "question": "What are the main findings?",
  "paper_id": "2301.12345"  // optional
}
```
**Response:**
```json
{
  "answer": "Based on the papers...",
  "sources": [
    {
      "id": "2301.12345",
      "content": "Relevant excerpt...",
      "metadata": {...}
    }
  ]
}
```

### POST /api/papers/save
**Purpose:** Save paper to library
**Query Params:** paper_id
**Response:**
```json
{
  "message": "Paper saved successfully",
  "paper_id": "2301.12345"
}
```

### GET /api/papers/saved
**Purpose:** Get all saved papers
**Response:**
```json
{
  "papers": [...]
}
```

### DELETE /api/papers/{paper_id}
**Purpose:** Delete saved paper
**Response:**
```json
{
  "message": "Paper deleted successfully"
}
```

## Database Schema

### ChromaDB Collections

#### research_papers Collection
- **Documents:** Paper title + abstract
- **Metadata:**
  - title: string
  - authors: string (comma-separated)
  - published: ISO date string
  - pdf_url: string
- **IDs:** arXiv paper ID
- **Embeddings:** Auto-generated by ChromaDB

## Security Considerations

1. **API Key Protection**
   - Store in .env file
   - Never commit to version control
   - Use environment variables

2. **CORS Configuration**
   - Restrict to specific origins
   - Currently allows localhost:3000

3. **Input Validation**
   - Pydantic models validate all inputs
   - Sanitize user queries

4. **Rate Limiting**
   - Implement for production
   - Prevent API abuse

## Performance Optimization

### Frontend
- React.memo for expensive components
- Lazy loading for large lists
- Debounce search inputs
- Cache API responses

### Backend
- Async/await for I/O operations
- Connection pooling
- Response caching
- Batch processing

### Database
- Vector indexing (HNSW)
- Efficient similarity search
- Persistent storage

## Scalability

### Horizontal Scaling
- Stateless backend design
- Load balancer ready
- Separate database server

### Vertical Scaling
- Optimize vector dimensions
- Increase ChromaDB resources
- Use faster embedding models

## Error Handling

### Frontend
- Try-catch blocks in API calls
- User-friendly error messages
- Loading states

### Backend
- HTTPException for API errors
- Detailed error logging
- Graceful degradation

## Testing Strategy

### Frontend Testing
- Component unit tests
- Integration tests for API calls
- E2E tests with Cypress

### Backend Testing
- Endpoint unit tests
- Service layer tests
- Integration tests with test database

## Monitoring & Logging

### Metrics to Track
- API response times
- Error rates
- User engagement
- OpenAI API usage
- Database query performance

### Logging Levels
- INFO: Normal operations
- WARNING: Potential issues
- ERROR: Failures
- DEBUG: Development details

## Future Enhancements

### Phase 1 (Short-term)
- [ ] User authentication
- [ ] PDF text extraction
- [ ] Advanced filtering
- [ ] Export functionality

### Phase 2 (Medium-term)
- [ ] Citation network visualization
- [ ] Collaborative workspaces
- [ ] Multiple LLM providers
- [ ] Custom embedding models

### Phase 3 (Long-term)
- [ ] Mobile app
- [ ] Browser extension
- [ ] Integration with reference managers
- [ ] Multi-language support

## Deployment Architecture

### Production Setup
```
┌─────────────┐
│   Vercel    │  ← Frontend (React)
└─────────────┘
       ↓
┌─────────────┐
│   Heroku    │  ← Backend (FastAPI)
└─────────────┘
       ↓
┌─────────────┐
│  PostgreSQL │  ← Metadata storage
└─────────────┘
       ↓
┌─────────────┐
│  ChromaDB   │  ← Vector storage
└─────────────┘
```

## Maintenance

### Regular Tasks
- Update dependencies monthly
- Monitor API usage
- Backup database weekly
- Review error logs
- Performance profiling

### Version Control
- Semantic versioning
- Feature branches
- Pull request reviews
- Automated testing

---

**Last Updated:** 2024
**Version:** 1.0.0
**Maintainer:** ResearchPilot Team
