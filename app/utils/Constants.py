from dotenv import load_dotenv
import os
load_dotenv()



# App
APP_NAME = "CreditSim"

# CORS Middleware
ALLOW_METHODS = ["OPTIONS", "POST", "GET"]
ALLOW_HEADERS = ["*"]
ALLOW_ORIGINS = ["https://creditaria-technical-test.fly.dev"]

# Amortization French Calculus
FIRST_PERIOD = 0
MIN_PERIOD_INTEREST_AMOUNT = 0
MIN_CAPITAL_PERIOD_AMORTIZATION_AMOUNT = 0
MONTHS_IN_YEAR = 12
ONE = 1
ZERO = 0

# Scoring Mockup  
MIN_DELAY_TIME = 3
MAX_DELAY_TIME = 3
FAILURE_PROBABILITY = 0.1
SCORING_FAILURE_MESSAGE = "Failure on scoring service"

# Connectors

USER = os.getenv("POSTGREDB_USER")
PASSWORD = os.getenv("POSTGREDB_PASSWORD")
HOST = os.getenv("POSTGREDB_HOST")
PORT = os.getenv("POSTGREDB_PORT")
DBNAME = os.getenv("POSTGREDB_NAME")

DATABASE_SQLITE_CONNECTION_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"
