from typing import List
from api.models.user import User
from fastapi import APIRouter, Depends, Body
from api.controllers.legal_proceeding import (
    delete_process,
    delete_processes,
    read_legal_proceeding,
)
from api.db.database import database as db
from api.security.authentication import get_user_admin_current

router = APIRouter()
legal_proceedings = db.legal_proceeding


@router.get("/legal_proceeding/")
def get_all_legal_proceedings(
    page: int = 1,
    page_size: int = 10,
    sort_by: str = None,
    order: str = "asc",
    search_field: str = None,
    search_value: str = None,
    user: User = Depends(get_user_admin_current),
):
    return read_legal_proceeding(
        page, page_size, sort_by, order, search_field, search_value
    )


@router.delete("/legal_proceeding/{process_id}")
def delete_process_id(process_id: str, user: User = Depends(get_user_admin_current)):
    return delete_process(process_id)


@router.delete("/legal_proceeding/")
def partial_delete_processes(
    ids: List[str] = Body(..., required=True),
    user: User = Depends(get_user_admin_current),
):
    return delete_processes(ids)
