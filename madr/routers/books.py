from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["books"])


@router.post("/")
def create_book(): ...


@router.get("/")
def read_books(): ...


@router.get("/{book_id}")
def read_book(book_id: int): ...


@router.patch("/{book_id}")
def update_book(book_id: int): ...


@router.delete("/{book_id}")
def delete_book(book_id: int): ...
