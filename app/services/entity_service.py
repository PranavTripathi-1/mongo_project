# app/services/entity_service.py

from app.models.entity import Entity, EntityResponse
from app.repository.mongo_repo import insert_entity, find_entity
from app.core.config import DB_NAME, COLLECTION_NAME

def add_entity_service(entity: Entity) -> EntityResponse:
    insert_entity(entity)
    return EntityResponse(
        name=entity.name,
        email=entity.email,
        database=DB_NAME,
        collection=COLLECTION_NAME
    )

def get_entity_service(name: str = None, email: str = None) -> EntityResponse:
    query = {}
    if name: query["name"] = name
    if email: query["email"] = email

    result = find_entity(query)
    if result:
        return EntityResponse(
            name=result["name"],
            email=result["email"],
            database=DB_NAME,
            collection=COLLECTION_NAME
        )
    return None
