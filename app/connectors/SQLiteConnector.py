from sqlmodel import SQLModel,create_engine, Session

# SQLite database URL (you can change this to use PostgreSQL, MySQL, etc.)
DATABASE_URL = "postgres:///./test.db"

# Create an engine and connect to the SQLite database
engine = create_engine(DATABASE_URL, echo=True)

# Create tables in the database
def create_db_and_tables():
    SQLModel.metadata.create_all(bind=engine)

# Create a session to interact with the database
def get_session():
    return Session(engine)