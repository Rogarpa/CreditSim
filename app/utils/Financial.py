from app.dtos.AmortizationCalculate import AmortizationCalculate

class Financial:
    def __init__(self) -> None:
        pass

    def calculate_first_period_french_amortization(self, amount, annual_rate, months_term):
        monthly_interest_rate = annual_rate/(12)
        return AmortizationCalculate(
            0,
            amount * (monthly_interest_rate/(1 - ((1+monthly_interest_rate)**(-months_term)))),
            monthly_interest_rate,
            0,
            0,
            amount
        )
        
    def calculate_period_french_amortization(self, last_amortization: AmortizationCalculate):
        if(last_amortization == None):
            return None
        
        actual_period_interest_amount = last_amortization.remain_balance_amount * last_amortization.interest_monthly_rate
        actual_period_amortization_amount = last_amortization.period_payment_amount - actual_period_interest_amount
        actual_amortization = AmortizationCalculate(
            last_amortization.actual_period+1,
            last_amortization.period_payment_amount,
            last_amortization.interest_monthly_rate,
            actual_period_interest_amount,
            actual_period_amortization_amount,
            last_amortization.remain_balance_amount - actual_period_amortization_amount
        )
        return actual_amortization