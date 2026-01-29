from app.dtos.AmortizationCalculate import AmortizationCalculate
from app.utils.Constants import *
class Financial:
    def __init__(self) -> None:
        pass

    def calculate_first_period_french_amortization(self, amount, annual_rate, months_term):
        monthly_interest_rate = annual_rate/(MONTHS_IN_YEAR)
        return AmortizationCalculate(
            FIRST_PERIOD,
            amount * (monthly_interest_rate/(ONE - ((ONE+monthly_interest_rate)**(-months_term)))),
            monthly_interest_rate,
            MIN_PERIOD_INTEREST_AMOUNT,
            MIN_CAPITAL_PERIOD_AMORTIZATION_AMOUNT,
            amount
        )
        
    def calculate_period_french_amortization(self, last_amortization: AmortizationCalculate):
        if(last_amortization == None):
            return None
        
        actual_period_interest_amount = last_amortization.remain_balance_amount * last_amortization.interest_monthly_rate
        actual_period_amortization_amount = last_amortization.period_payment_amount - actual_period_interest_amount
        actual_amortization = AmortizationCalculate(
            last_amortization.actual_period+ONE,
            last_amortization.period_payment_amount,
            last_amortization.interest_monthly_rate,
            actual_period_interest_amount,
            actual_period_amortization_amount,
            last_amortization.remain_balance_amount - actual_period_amortization_amount
        )
        return actual_amortization