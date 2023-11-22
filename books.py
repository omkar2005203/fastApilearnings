from fastapi import Body,FastAPI


app = FastAPI()


BOOKS = [
    {'title':'title one','author':'author one','category':'science'},
    {'title':'title two','author':'author two','category':'math'},
    {'title':'title three','author':'author three','category':'history'},
    {'title':'title four','author':'author four','category':'geography'}
]


### GET API 

@app.get("/")
async def first_api():
    return {"message":"hello omkar !"}


@app.get("/api")
async def first_api():
    return {"message":"hello omkar on api endpoint !"}

@app.get("/books")
async def reall_all_book():
    return BOOKS

# @app.get("/books/{dynamic_param}")
# async def read_all_books(dynamic_param:str):
#     return {'dynamic_param':dynamic_param}


@app.get("/books/{book_title}")
async def read_books(book_title: str):
    print(f"This is dyanmic url var : {book_title}")
    for book in BOOKS:
        print(book.get('title').casefold())
        if book.get('title').casefold() == book_title.casefold():
            print("this is working")
            return book
        print("this is not working !")


# query and path parameters
@app.get("/books/{author_name}/")
async def read_cat_auth(author_name: str,category: str):
    data = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold() and book.get("category").casefold() == category.casefold():
            data.append(book)

        return data

## QUERY parameter example
@app.get("/books/")
async def read_book(category: str):
    data = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            data.append(book)
    return book

#POST
@app.post('/books/create_book')
async def create_book(new_book = Body()):
    BOOKS.append(new_book)


@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book


@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title : str):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book_title.casefold():
            BOOKS.pop(i)
            break

## Assignment -1 fetch books using author name 

## using path parameter
@app.get("/books_new/{author_name}")
async def get_author(author_name :str):
    data = []
    for book in BOOKS:
        if book.get('author').casefold() == author_name.casefold():
            data.append(book)
    return data


## query parameter
@app.get("/books_new")
async def get_author(author: str):
    data = []
    for book in BOOKS:
        if book.get('author').casefold() == author.casefold():
            data.append(book)
        
    return data



