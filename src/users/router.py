from fastapi import APIRouter
from .service import router

users_router = APIRouter()
users_router.include_router(
    router=router
)