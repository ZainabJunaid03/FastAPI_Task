from fastapi import FastAPI, Request, Depends, HTTPException, status
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from .views import router as user_router
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")
    

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(user_router)
