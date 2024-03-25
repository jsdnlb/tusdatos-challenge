from typing import List
from api.models.user import User, UserDeleteResponse, UserResponse
from fastapi import APIRouter, Body, Depends
from api.controllers.user import (
    read_all_user,
    get_user,
    create_user,
    update_user,
    delete_user,
    delete_specific_user,
)
from api.db.database import database as db
from api.security.authentication import get_user_disabled_current

router = APIRouter()
users = db.users


@router.get("/users/", response_model=UserResponse)
def get_all_users(user: User = Depends(get_user_disabled_current)):
    return read_all_user()


@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: str, user: User = Depends(get_user_disabled_current)):
    return get_user(user_id)


@router.post("/users/", response_model=User)
def create_user_route(new_user: User, user: User = Depends(get_user_disabled_current)):
    return create_user(new_user)


@router.put("/users/{user_id}", response_model=User)
def update_user_all(
    user_id: str, updated_user: User, user: User = Depends(get_user_disabled_current)
):
    return update_user(user_id, updated_user)


@router.patch("/users/{user_id}", response_model=User)
def patch_user(
    user_id: str, updated_user: User, user: User = Depends(get_user_disabled_current)
):
    return update_user(user_id, updated_user)


@router.delete("/users/{user_id}", response_model=User)
def delete_user_id(user_id: str, user: User = Depends(get_user_disabled_current)):
    return delete_user(user_id)


@router.delete("/users/", response_model=UserDeleteResponse)
def partial_delete_user(
    ids: List[str] = Body(..., required=True),
    user: User = Depends(get_user_disabled_current),
):
    return delete_specific_user(ids)
