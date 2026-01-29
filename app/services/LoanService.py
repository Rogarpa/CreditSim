from app.dtos.AmortizationPeriods import AmortizationPeriods
from app.dtos.AmortizationRequest import AmortizationRequest
from app.utils.Financial import Financial
from app.repositories.AmortizationRepository import AmortizationRepository
from app.services.ScoringService import ScoringService
from app.services.ServiceWrapper import ServiceWrapper
import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

from fastapi import BackgroundTasks
class LoanService:
    async def get_amortization_french_periods(self, amortization_request: AmortizationRequest, background_tasks: BackgroundTasks):
        amortization_periods = AmortizationPeriods()
        financial = Financial()

        if(amortization_request.monto <=0 or amortization_request.tasa_anual <=0 or amortization_request.plazo_meses <=0):
            return amortization_periods
        
        last_period_amortization = financial.calculate_first_period_french_amortization(amortization_request.monto, amortization_request.tasa_anual, amortization_request.plazo_meses)
        amortization_periods.amortization_periods.append(last_period_amortization)

        for i in range(amortization_request.plazo_meses):
            last_period_amortization = financial.calculate_period_french_amortization(last_period_amortization)
            amortization_periods.amortization_periods.append(last_period_amortization)
        
        background_tasks.add_task(AmortizationRepository.create_amortization,amortization_request, amortization_periods)
    
        service_wrapper = ServiceWrapper((lambda e : logger.error(e)), ScoringService().notificate)
        background_tasks.add_task(service_wrapper.execute_service)
      
        return amortization_periods
    
    async def get_amortization_french_list():
        return await AmortizationRepository.list_amortization()