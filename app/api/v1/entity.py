# app/api/v1/entity.py

from fastapi import APIRouter, Query, HTTPException
from app.models.entity import Entity, EntityResponse
from app.services.entity_service import add_entity_service, get_entity_service

router = APIRouter(prefix="/entity", tags=["Entity"])

@router.post("/add", response_model=EntityResponse)
def add_entity(entity: Entity):
    return add_entity_service(entity)

@router.get("/get", response_model=EntityResponse)
def get_entity(name: str = Query(None), email: str = Query(None)):
    result = get_entity_service(name, email)
    if not result:
        raise HTTPException(status_code=404, detail="Entity not found")
    return result
