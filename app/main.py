from app.dtos.AmortizationRequest import AmortizationRequest
from app.dtos.AmortizationResponse import AmortizationResponse
from app.utils.Constants import *

from fastapi import FastAPI, BackgroundTasks, HTTPException
from app.connectors.SQLiteConnector import create_db_and_tables
from app.services.LoanService import LoanService
from app.mappers.AmortizationMapper import AmortizationMapper
from fastapi.middleware.cors import CORSMiddleware
create_db_and_tables()
app = FastAPI(title=APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOW_ORIGINS,
    allow_credentials=True,
    allow_methods=[ALLOW_METHODS],
    allow_headers=[ALLOW_HEADERS],
)
@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/simulate")
async def simulate(amortization_request: AmortizationRequest, background_tasks: BackgroundTasks):
    loan_service = LoanService()
    try:
        amortization_table = await loan_service.get_amortization_french_periods(amortization_request, background_tasks)
        return amortization_table
    except ValueError as e:
        raise HTTPException(status_code=422, detail="Illegal arguments semantic")
        


@app.get("/simulate", response_model=list[AmortizationResponse])
async def get_simulations():
    loan_service = LoanService()
    return map(AmortizationMapper.amortizationdb_to_amortizationresponse, await loan_service.get_amortization_french_list())

@app.options("/simulate")
async def get_options_simulate():
    return ""