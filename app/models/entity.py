# app/models/entity.py

from pydantic import BaseModel

class Entity(BaseModel):
    name: str
    email: str

class EntityResponse(Entity):
    database: str
    collection: str
