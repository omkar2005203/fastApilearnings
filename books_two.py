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
    published_date: int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class  BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed')
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1,max_length=100)
    rating: int = Field(gt=-1,lt=6)
    published_date: int

    class Config:
        json_schema_extra = {
           'example': {
            'title':'A new book',
            'author':'abc',
            'description':'A new description for book',
            'rating':5
           }

        }



        
BOOKS = [Book(1,'CS','omkar','A nice book',6,2012),Book(2,'CS','omkar','A nice book',5,2013),Book(3,'CS','omkar','A nice book',7,2023)]

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


@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book
        

@app.get("/books/")
async def get_book_rating(book_rating: int):
    for book in BOOKS:
        if book.rating == book_rating:
            return book
        

@app.put('/books/update_book')
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete('/books/book_delete/{book_id}')
async def book_delete(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break

@app.get('/books/search_by_year/{published_year}')
async def find_out_book(published_year: int):
    data = []
    for book in BOOKS:
        print(f"loop {book.published_date}")
        print(f"Path param: {published_year}")
        if book.published_date == published_year:
            data.append(book)
            return data
