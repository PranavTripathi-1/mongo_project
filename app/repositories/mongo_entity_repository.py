from typing import Optional
from app.entities.entity import Entity
from app.interfaces.entity_repository import EntityRepository
from pymongo import MongoClient
from app.core.config import settings

class MongoEntityRepository(EntityRepository):
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URI)
        self.collection = self.client[settings.DB_NAME]["entities"]

    def insert(self, entity: Entity) -> dict:
        result = self.collection.insert_one(entity.dict())
        return {"inserted_id": str(result.inserted_id)}

    def find_by_name_or_email(self, name: Optional[str] = None, email: Optional[str] = None) -> Optional[dict]:
        query = {}
        if name:
            query["name"] = name
        if email:
            query["email"] = email
        return self.collection.find_one(query, {"_id": 0})
