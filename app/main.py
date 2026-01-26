from fastapi import FastAPI
from app.models.dtos.AmortizationRequest import AmortizationRequest

from fastapi import FastAPI
from app.connectors.SQLiteConnector import create_db_and_tables
from app.services.LoanService import LoanService

create_db_and_tables()
app = FastAPI(title="CreditSim")


@app.get("/health")
def health():
    return {"status": "ok"}



@app.post("/simulate")
async def create_item(amortization_request: AmortizationRequest):
    amortization_table = LoanService().get_amortization_french_periods(amortization_request)
    return amortization_table

