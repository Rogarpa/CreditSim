from fastapi import FastAPI
from app.models.dtos.AmortizationRequest import AmortizationRequest

app = FastAPI(title="CreditSim")


@app.get("/health")
def health():
    return {"status": "ok"}



@app.post("/simulate")
async def create_item(amortization_request: AmortizationRequest):
    return amortization_request