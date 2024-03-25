from api.models.user import User
from fastapi import APIRouter, Depends
from api.controllers.legal_proceeding import (
    read_legal_proceeding,
)
from api.db.database import database as db
from api.security.authentication import get_user_admin_current

router = APIRouter()
legal_proceedings = db.legal_proceeding


@router.get("/legal_proceeding/")
def get_all_legal_proceedings(
    page: int = 1, page_size: int = 10, user: User = Depends(get_user_admin_current)
):
    return read_legal_proceeding(page, page_size)
