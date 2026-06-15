from pydantic import BaseModel


class SustainabilityRequest(BaseModel):
    city: str
    question: str