from fastapi import FastAPI
from app.models.dtos.AmortizationRequest import AmortizationRequest

from fastapi import FastAPI, BackgroundTasks
from app.connectors.SQLiteConnector import create_db_and_tables
from app.services.LoanService import LoanService
from fastapi.middleware.cors import CORSMiddleware
from time import sleep
create_db_and_tables()
app = FastAPI(title="CreditSim")



# Define the list of allowed origins (e.g., your frontend application's URL)
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

@app.get("/health")
def health():
    return {"status": "ok"}



@app.post("/simulate")
async def create_item(amortization_request: AmortizationRequest, background_tasks: BackgroundTasks):
    amortization_table = await LoanService().get_amortization_french_periods(amortization_request, background_tasks)
    return amortization_table

