from fastapi import FastAPI


app = FastAPI()


BOOKS = [
    {'title':'title one','author':'author one','category':'science'},
    {'title':'title two','author':'author two','category':'math'},
    {'title':'title three','author':'author three','category':'history'},
    {'title':'title four','author':'author four','category':'geography'}
]

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



@app.get("/books/{author_name}/")
async def read_cat_auth(author_name: str,category: str):
    data = []
    for book in BOOKS:
        if book.get("author").casefold() == author_name.casefold() and book.get("category").casefold() == category.casefold():
            data.append(book)

        return data
