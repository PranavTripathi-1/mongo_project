# app/main.py

from fastapi import FastAPI
from app.api.v1 import entity

app = FastAPI(title="MongoDB Clean Architecture API")

app.include_router(entity.router)

@app.get("/")
def root():
    return {"message": "Clean Architecture MongoDB API 👋"}
