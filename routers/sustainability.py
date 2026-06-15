from fastapi import APIRouter, HTTPException

from schemas.request_models import SustainabilityRequest
from schemas.response_models import AnalyzeResponse

from agents.orchestrator import orchestrator

router = APIRouter()


@router.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze(request: SustainabilityRequest):

    try:

        return orchestrator(
            city=request.city,
            question=request.question
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )