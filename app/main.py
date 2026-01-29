from app.dtos.AmortizationRequest import AmortizationRequest
from app.dtos.AmortizationResponse import AmortizationResponse
from app.utils.Constants import *

from fastapi import FastAPI, BackgroundTasks
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
    amortization_table = await LoanService().get_amortization_french_periods(amortization_request, background_tasks)
    return amortization_table


@app.get("/simulate", response_model=list[AmortizationResponse])
async def get_simulations():
    return map(AmortizationMapper.amortizationdb_to_amortizationresponse, await LoanService.get_amortization_french_list())

@app.options("/simulate")
async def get_options_simulate():
    return ""