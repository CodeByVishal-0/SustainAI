from pydantic import BaseModel
from typing import List, Dict, Any


class AnalyzeResponse(BaseModel):
    city: str
    weather: Dict[str, Any]
    impact: Dict[str, Any]
    news: List[Dict[str, Any]]
    rag_insights: str
    report: str