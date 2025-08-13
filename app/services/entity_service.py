from typing import Optional
from app.entities.entity import Entity
from app.interfaces.entity_repository import EntityRepository

class EntityService:
    def __init__(self, repository: EntityRepository):
        self.repository = repository

    def add_entity(self, entity: Entity) -> dict:
        return self.repository.insert(entity)

    def get_entity(self, name: Optional[str], email: Optional[str]) -> dict:
        result = self.repository.find_by_name_or_email(name, email)
        return result or {"message": "Entity not found"}
