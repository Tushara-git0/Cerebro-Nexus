from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from services.paper_service import PaperService
from services.vector_service import VectorService
from services.llm_service import LLMService

load_dotenv()

app = FastAPI(title="ResearchPilot AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

paper_service = PaperService()
vector_service = VectorService()
llm_service = LLMService()

class SearchRequest(BaseModel):
    query: str
    max_results: int = 10

class QuestionRequest(BaseModel):
    question: str
    paper_id: Optional[str] = None

class SummarizeRequest(BaseModel):
    paper_id: str

@app.get("/")
def root():
    return {"message": "ResearchPilot AI - Autonomous Research Intelligence Hub"}

@app.post("/api/search")
async def search_papers(request: SearchRequest):
    try:
        papers = await paper_service.search_papers(request.query, request.max_results)
        return {"papers": papers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/summarize")
async def summarize_paper(request: SummarizeRequest):
    try:
        paper = await paper_service.get_paper(request.paper_id)
        summary = await llm_service.summarize(paper)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/question")
async def ask_question(request: QuestionRequest):
    try:
        if request.paper_id:
            context = await vector_service.get_relevant_context(request.question, request.paper_id)
        else:
            context = await vector_service.search_all(request.question)
        
        answer = await llm_service.answer_question(request.question, context)
        return {"answer": answer, "sources": context}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/papers/save")
async def save_paper(paper_id: str):
    try:
        paper = await paper_service.get_paper(paper_id)
        await vector_service.store_paper(paper)
        return {"message": "Paper saved successfully", "paper_id": paper_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/papers/saved")
async def get_saved_papers():
    try:
        papers = await vector_service.get_all_papers()
        return {"papers": papers}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/papers/{paper_id}")
async def delete_paper(paper_id: str):
    try:
        await vector_service.delete_paper(paper_id)
        return {"message": "Paper deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
