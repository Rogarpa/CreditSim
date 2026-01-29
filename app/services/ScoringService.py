from random import random,uniform
from asyncio import sleep
from app.exceptions.ScoringException import ScoringException
from app.utils.Constants import *
class ScoringService:
    async def notificate(self):
        delay_time = uniform(MIN_DELAY_TIME, MAX_DELAY_TIME)
        failure_probability = FAILURE_PROBABILITY
        failure_posibility = random()
        await sleep(delay_time)
        if(failure_posibility <= failure_probability):
            raise ScoringException(SCORING_FAILURE_MESSAGE)
            
        