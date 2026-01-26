from app.models.dtos.AmortizationPeriods import AmortizationPeriods
from app.models.dtos.AmortizationRequest import AmortizationRequest
from app.utils.Financial import Financial
from app.repositories.AmortizationRepository import AmortizationRepository

class LoanService:
    def get_amortization_french_periods(self, amortization_request: AmortizationRequest):
        amortization_periods = AmortizationPeriods()
        financial = Financial()
        if(amortization_request.monto <=0 or amortization_request.tasa_anual <=0 or amortization_request.plazo_meses <=0):
            print("Failure")
            return amortization_periods
        last_period_amortization = financial.calculate_first_period_french_amortization(amortization_request.monto, amortization_request.tasa_anual, amortization_request.plazo_meses)
        amortization_periods.amortization_periods.append(last_period_amortization)

        for i in range(amortization_request.plazo_meses):
            last_period_amortization = financial.calculate_period_french_amortization(last_period_amortization)
            amortization_periods.amortization_periods.append(last_period_amortization)

        AmortizationRepository.create_amortization(amortization_request, amortization_periods)

        return amortization_periods
            