from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf.db import SQLALCHEMY_DATABASE_URL

app = FastAPI()

# Set up the database
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/check_db")
def check_db():
    try:
        # Attempt to connect to the database
        db = SessionLocal()
        db.execute("SELECT 1")
        return {"message": "Database connection successful!"}
    except Exception as e:
        return {"message": f"Database connection failed: {str(e)}"}
