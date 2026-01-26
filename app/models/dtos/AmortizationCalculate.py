from dataclasses import dataclass

class AmortizationCalculate:
    actual_period: int 
    period_payment_amount: float
    
    interest_monthly_rate: float
    period_interest_amount: float

    capital_period_amortization_amount: float

    remain_balance_amount: float


    def __init__(self,
                actual_period,
                period_payment_amount,
                interest_monthly_rate,
                period_interest_amount,
                capital_period_amortization_amount,
                remain_balance_amount
                ):
        self.actual_period = actual_period
        self.period_payment_amount = period_payment_amount
        self.interest_monthly_rate = interest_monthly_rate
        self.period_interest_amount = period_interest_amount
        self.capital_period_amortization_amount = capital_period_amortization_amount
        self.remain_balance_amount = remain_balance_amount

