from fastapi import FastAPI ,Body
from pydantic import BaseModel,Field
from typing import Optional

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
    id: Optional[int]
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1,max_length=100)
    rating: int = Field(gt=-1,lt=6)



        
BOOKS = [Book(1,'CS','omkar','A nice book',5),Book(2,'CS','omkar','A nice book',5),Book(3,'CS','omkar','A nice book',5)]

@app.get("/books")
async def read_all_books():
    return BOOKS


# @app.post("/create-book")
# async def create_book(book_req = Body()):
#     BOOKS.append(book_req)


# @app.post("/create-book")
# async def create_book(book_req: BookRequest):
#     BOOKS.append(book_req)

@app.post("/create-book")
async def create_book(book_req: BookRequest):
    new_book = Book(**book_req.dict())
    BOOKS.append(find_book_id(new_book))



def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book