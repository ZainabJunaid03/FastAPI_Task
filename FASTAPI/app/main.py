from fastapi import FastAPI, Depends, HTTPException, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .views import router as user_router

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user_router)
