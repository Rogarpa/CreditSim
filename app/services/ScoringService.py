from random import random,uniform
from asyncio import sleep
from app.exceptions.ScoringException import ScoringException

class ScoringService:
    async def notificate(self):
        delay_time = uniform(1, 3)
        failure_probability = 0.1
        failure_posibility = random()
        await sleep(delay_time)
        if(failure_posibility <= failure_probability):
            raise ScoringException("Failure on scoring service")
            
        