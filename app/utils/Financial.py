from app.dtos.AmortizationCalculate import AmortizationCalculate
from app.utils.Constants import *
class Financial:
    def __init__(self) -> None:
        pass

    def calculate_first_period_french_amortization(self, amount, annual_rate, months_term):
        monthly_interest_rate = annual_rate/(MONTHS_IN_YEAR)
        return AmortizationCalculate(
            FIRST_PERIOD,
            round(amount * (monthly_interest_rate/(ONE - ((ONE + monthly_interest_rate)**( - months_term)))),2),
            round(monthly_interest_rate, 2),
            round(MIN_PERIOD_INTEREST_AMOUNT, 2),
            round(MIN_CAPITAL_PERIOD_AMORTIZATION_AMOUNT, 2),
            round(amount, 2)
        )
        
    def calculate_period_french_amortization(self, last_amortization: AmortizationCalculate):
        if(last_amortization == None):
            return None
        
        actual_period_interest_amount = round(last_amortization.remain_balance_amount * last_amortization.interest_monthly_rate, 2)
        actual_period_amortization_amount = round(last_amortization.period_payment_amount - actual_period_interest_amount, 2)
        reamain_balance_amount = last_amortization.remain_balance_amount - actual_period_amortization_amount
        
        actual_amortization = AmortizationCalculate(
            last_amortization.actual_period + ONE,
            last_amortization.period_payment_amount,
            last_amortization.interest_monthly_rate,
            actual_period_interest_amount,
            actual_period_amortization_amount,
            round((0 if(reamain_balance_amount < 0) else reamain_balance_amount), 2)
        )
        return actual_amortization