# app/repository/mongo_repo.py

from app.core.config import db, COLLECTION_NAME
from app.models.entity import Entity

collection = db[COLLECTION_NAME]

def insert_entity(entity: Entity):
    return collection.insert_one(entity.dict())

def find_entity(query: dict):
    return collection.find_one(query)
