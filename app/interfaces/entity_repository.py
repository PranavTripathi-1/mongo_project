from abc import ABC, abstractmethod
from typing import Optional
from app.entities.entity import Entity

class EntityRepository(ABC):
    @abstractmethod
    def insert(self, entity: Entity) -> dict:
        pass

    @abstractmethod
    def find_by_name_or_email(self, name: Optional[str] = None, email: Optional[str] = None) -> Optional[dict]:
        pass
