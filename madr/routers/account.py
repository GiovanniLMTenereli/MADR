from fastapi import APIRouter

router = APIRouter(prefix="/account", tags=["account"])


@router.post("/")
def create_account(): ...


@router.put("/{account_id}")
def update_account(): ...


@router.delete("/{account_id}")
def delete_account(): ...
