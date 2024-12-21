from pydantic import BaseModel


class BooksSchema(BaseModel):
    title: str
    year: int
    writer_id: int


class ReturnableBook(BooksSchema):
    id: int


class BooksList(BaseModel):
    books: list[ReturnableBook]
