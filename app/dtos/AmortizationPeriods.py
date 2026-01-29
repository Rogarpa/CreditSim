from app.dtos.AmortizationCalculate import AmortizationCalculate

class AmortizationPeriods():
    amortization_periods: list[AmortizationCalculate]
    def __init__(self) -> None:
        self.amortization_periods = []