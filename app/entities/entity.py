from pydantic import BaseModel, EmailStr

class Entity(BaseModel):
    name: str
    email: EmailStr
