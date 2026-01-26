from app.models.dtos.AmortizationPeriods import AmortizationPeriods
from app.models.dtos.AmortizationRequest import AmortizationRequest
from app.models.dtos.AmortizationDB import AmortizationDB
from app.connectors.SQLiteConnector import get_session, create_db_and_tables
from fastapi.encoders import jsonable_encoder

class AmortizationRepository():

    def create_amortization(amortization_request: AmortizationRequest,amortization_periods: AmortizationPeriods):
        session = get_session()
        amortization_db = AmortizationDB(
            amount=amortization_request.monto,
            annual_rate=amortization_request.tasa_anual,
            months_term=amortization_request.plazo_meses,
            amortization_table=str(jsonable_encoder(amortization_periods.amortization_periods))
        )
        try:
            session.add(amortization_db)
            session.commit()
            session.refresh(amortization_db)
        except:
            session.rollback()
            return False
        finally:
            session.close()
        return True