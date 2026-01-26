from app.models.dtos.AmortizationPeriods import AmortizationPeriods
from app.utils.Financial import Financial

class LoanEngine:
    def get_amortization_french_periods(self, amount, annual_rate, months_term):
        amortization_periods = AmortizationPeriods()
        financial = Financial()
        if(amount <=0 or annual_rate <=0 or months_term <=0):
            return amortization_periods
        last_period_amortization = financial.calculate_first_period_french_amortization(amount, annual_rate, months_term)
        amortization_periods.amortization_periods.append(last_period_amortization)

        for i in range(months_term):
            last_period_amortization = financial.calculate_period_french_amortization(last_period_amortization)
            amortization_periods.amortization_periods.append(last_period_amortization)
        return amortization_periods
            