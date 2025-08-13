from fastapi import FastAPI
from app.api import entity_routes

app = FastAPI(title="Clean Architecture MongoDB API")

app.include_router(entity_routes.router)
