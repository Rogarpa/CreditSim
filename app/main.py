from app.dtos.AmortizationRequest import AmortizationRequest

from fastapi import FastAPI, BackgroundTasks
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.connectors.SQLiteConnector import get_session
from app.connectors.SQLiteConnector import create_db_and_tables
from app.models.dtos.AmortizationDB import AmortizationDB
from app.services.LoanService import LoanService
from fastapi.middleware.cors import CORSMiddleware
create_db_and_tables()
app = FastAPI(title="CreditSim")

origins = [
        "*"

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/simulate")
async def simulate(amortization_request: AmortizationRequest, background_tasks: BackgroundTasks):
    amortization_table = await LoanService().get_amortization_french_periods(amortization_request, background_tasks)
    return amortization_table


@app.get("/simulate", response_model=list[AmortizationDB])
async def get_simulations():
    return await LoanService.get_amortization_french_list();

@app.options("/simulate")
async def get_options_simulate():
    return ""