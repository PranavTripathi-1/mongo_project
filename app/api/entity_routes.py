from fastapi import APIRouter, Depends
from app.entities.entity import Entity
from app.services.entity_service import EntityService
from app.repositories.mongo_entity_repository import MongoEntityRepository

router = APIRouter()

# Dependency injection
def get_entity_service():
    repo = MongoEntityRepository()
    return EntityService(repo)

@router.post("/entity/add")
def add_entity(entity: Entity, service: EntityService = Depends(get_entity_service)):
    return service.add_entity(entity)

@router.get("/entity/get")
def get_entity(name: str = None, email: str = None, service: EntityService = Depends(get_entity_service)):
    return service.get_entity(name, email)
