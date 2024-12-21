from fastapi import FastAPI

from madr.routers import account, books, token, writers

app = FastAPI()

app.include_router(writers.router)
app.include_router(books.router)
app.include_router(account.router)
app.include_router(token.router)


@app.get("/")
def read_root():
    return {"Message": "Hello World"}
