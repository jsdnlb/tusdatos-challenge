from uuid import uuid4
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class User(BaseModel):
    id: str = Field(default_factory=uuid4, alias="_id")
    username: Optional[str] = None
    age: Optional[int] = None
    role: Optional[str] = None
    full_name: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None
    disabled: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        __collection__ = "users"
        pooulate_by_name = True
        json_schema_extra = {
            "username": "user",
            "full_name": "Test user",
            "age": 32,
            "role": "client",
            "email": "user@example.com",
            "hashed_password": "secret",
            "disabled": False,
        }


class UserResponse(BaseModel):
    message: str
    users_ids: List[str]
    result: List[User]


class UserDeleteResponse(BaseModel):
    message: str
    deleted_count: int
