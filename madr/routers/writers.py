from fastapi import APIRouter

router = APIRouter(prefix="/writers", tags=["writers"])


@router.post("/")
def create_writer(): ...


@router.get("/")
def read_writers(): ...


@router.get("/{writer_id}")
def read_writer(writer_id: int): ...


@router.patch("/{writer_id}")
def update_writer(writer_id: int): ...


@router.delete("/{writer_id}")
def delete_writer(writer_id: int): ...
