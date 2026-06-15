from fastapi import APIRouter

from schemas.request_models import SustainabilityRequest

from agents.orchestrator import orchestrator

router = APIRouter()


from fastapi import HTTPException


@router.post("/analyze")
def analyze(request: SustainabilityRequest):

    try:

        report = orchestrator(
            city=request.city,
            question=request.question
        )

        return {
            "status": "success",
            "report": report
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )