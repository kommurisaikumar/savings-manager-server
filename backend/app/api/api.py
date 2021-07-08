from fastapi import APIRouter
from app.api.end_points import users, transactions, categories, accounts

router = APIRouter()

router.include_router(
    users.router,
    prefix="/user",
    tags=["user"]
)

router.include_router(
    transactions.router,
    prefix="/transaction",
    tags=["transaction"]
)

router.include_router(
    categories.router,
    prefix="/category",
    tags=["categories"],
)

router.include_router(
    accounts.router,
    prefix="/account",
    tags=["account"]
)
