from pydantic import BaseModel
from app.models.dtos.AmortizationPeriods import AmortizationPeriods

class AmortizationRequestDB(BaseModel):
    amount: float
    annual_rate: float
    months_term: int
    json: str