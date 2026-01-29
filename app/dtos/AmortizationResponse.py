from pydantic import BaseModel

class AmortizationResponse(BaseModel):
    id: int
    monto: float
    tasa_anual: float
    plazo_meses: int
    amortization_table: str