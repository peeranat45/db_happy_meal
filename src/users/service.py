from fastapi import APIRouter
from src.dependencies import SessionDep

router = APIRouter(tags=["users"])

@router.post("/")
def create_user(

) -> None:
    pass


@router.get("/profile")
def get_user(
    session: SessionDep
) -> None:
    pass