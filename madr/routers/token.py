from fastapi import APIRouter

router = APIRouter(prefix="/token", tags=["token"])


@router.post("/")
def create_token(): ...


@router.post("/refresh_token")
def refresh_token(): ...
