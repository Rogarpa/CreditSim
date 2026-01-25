from pydantic import BaseModel

class AmortizationRequest(BaseModel):
    monto: float
    tasa_anual: float
    plazo_meses: float