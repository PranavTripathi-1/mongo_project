import pytest
from app.entities.entity import Entity
from app.services.entity_service import EntityService
from app.interfaces.entity_repository import EntityRepository


# Fake Repository for Testing
class FakeEntityRepository(EntityRepository):
    def __init__(self):
        self.storage = []

    def insert(self, entity: Entity) -> dict:
        self.storage.append(entity.dict())
        return {"inserted_id": len(self.storage)}

    def find_by_name_or_email(self, name=None, email=None):
        for item in self.storage:
            if (name and item["name"] == name) or (email and item["email"] == email):
                return item
        return None


@pytest.fixture
def service():
    repo = FakeEntityRepository()
    return EntityService(repo)


def test_add_entity(service):
    entity = Entity(name="John Doe", email="john@example.com")
    result = service.add_entity(entity)
    assert result["inserted_id"] == 1


def test_get_entity_by_name(service):
    entity = Entity(name="Jane Doe", email="jane@example.com")
    service.add_entity(entity)

    result = service.get_entity(name="Jane Doe", email=None)
    assert result["name"] == "Jane Doe"
    assert result["email"] == "jane@example.com"


def test_get_entity_not_found(service):
    result = service.get_entity(name="Ghost", email=None)
    assert result == {"message": "Entity not found"}
