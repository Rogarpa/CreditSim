from sqlmodel import SQLModel,create_engine, Session
from app.utils.Constants import *

engine = create_engine(DATABASE_SQLITE_CONNECTION_URL, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    return Session(engine)