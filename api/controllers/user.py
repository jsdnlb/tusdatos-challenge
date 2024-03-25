from typing import List
from fastapi.encoders import jsonable_encoder
from api.models.user import User, UserResponse, UserDeleteResponse
from api.db.database import database
from passlib.context import CryptContext
from datetime import datetime

from api.utils.exception_handler import exception_handler

now = datetime.now()
users = database.users
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def read_all_user() -> UserResponse:
    all_records = [x for x in users.find()]
    cleaned_users = [{**user, "_id": str(user["_id"])} for user in all_records]
    user_ids = [str(user["_id"]) for user in all_records]
    return {
        "message": "List of users",
        "users_ids": user_ids,
        "result": cleaned_users,
    }


def get_user(user_id: str) -> User:
    user_data = users.find_one({"_id": user_id})
    if not user_data:
        raise exception_handler("404_NOT_FOUND")
    return User(**user_data)


def create_user(user: User) -> User:
    hash = pwd_context.hash(user.hashed_password)
    user.hashed_password = hash
    user.created_at = datetime.timestamp(now)
    result = users.insert_one(jsonable_encoder(user))
    created_user = users.find_one({"_id": result.inserted_id})
    return User(**created_user)


def update_user(user_id: str, updated_user: User) -> User:
    existing_user = users.find_one({"_id": user_id})
    if not existing_user:
        raise exception_handler("404_NOT_FOUND")
    update_data = updated_user.dict(exclude_unset=True)
    update_data["updated_at"] = datetime.timestamp(now)
    users.update_one({"_id": user_id}, {"$set": update_data})
    updated_user_data = users.find_one({"_id": user_id})
    return User(**updated_user_data)


def delete_user(user_id: str) -> User:
    existing_user = users.find_one({"_id": user_id})
    if not existing_user:
        raise exception_handler("404_NOT_FOUND")
    users.delete_one({"_id": user_id})
    return User(**existing_user)


def delete_specific_user(user_ids: List[str]) -> UserDeleteResponse:
    if not user_ids:
        raise exception_handler("422_NO_ID")
    deleted_count = users.delete_many({"_id": {"$in": user_ids}})
    if deleted_count.deleted_count == 0:
        raise exception_handler("404_NOT_FOUND")

    return {
        "message": "User deleted",
        "deleted_count": deleted_count.deleted_count,
    }
