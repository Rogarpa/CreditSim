from app.services.ScoringService import ScoringService

class ServiceWrapper():
    def __init__(self, callback, service_function):
        self.callback = callback
        self.service_function = service_function
    
    async def execute_service(self):
        try:
            await self.service_function()
        except Exception as e:
            self.callback(e)