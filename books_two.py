from fastapi import FastAPI ,Body
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: str
    title: str
    author: str
    description: str
    rating: int

    def __init__(self,id,title,author,description,rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class  BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int



        
BOOKS = [Book(1,'CS','omkar','A nice book',5),Book(2,'CS','omkar','A nice book',5),Book(3,'CS','omkar','A nice book',5)]

@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.post("/create-book")
# async def create_book(book_req = Body()):
#     BOOKS.append(book_req)


@app.post("/create-book")
async def create_book(book_req: BookRequest):
    BOOKS.append(book_req)