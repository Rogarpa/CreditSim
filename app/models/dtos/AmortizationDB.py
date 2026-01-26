from sqlmodel import SQLModel, Field
from datetime import datetime
from app.models.dtos.AmortizationPeriods import AmortizationPeriods

class AmortizationDB(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    amount: float
    annual_rate: float
    months_term: int
    amortization_table: str