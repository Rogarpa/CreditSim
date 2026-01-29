from app.dtos.AmortizationResponse import AmortizationResponse
from app.models.AmortizationDB import AmortizationDB
class AmortizationMapper():
    def amortizationdb_to_amortizationresponse(amortizationdb: AmortizationDB):
        return AmortizationResponse(
            id= amortizationdb.id,
            monto=amortizationdb.amount,
            tasa_anual=amortizationdb.annual_rate,
            plazo_meses=amortizationdb.months_term,
            amortization_table=amortizationdb.amortization_table
        )