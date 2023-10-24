from fastapi import FastAPI, Body

app = FastAPI()

@app.get("/api")
def get_api():
    return {"message": "Hello World!"}

@app.get("/books/{path_param}")
def get_api_with_path_param(path_param: str):
    return {"message": f"Hello {path_param}"}

@app.get("/books/")
def get_api_with_query_param(title: str):
    return {"message": f"Hello {title}"}

@app.get("/books/{path_param}/")
def get_api_with_path_and_query_params(path_param: str, title: str):
    return {"message": f"Hello {path_param}, {title}"}

@app.post("/books/create_book")
def post_create_book(new_book: dict):
    # Here, `new_book` should be a dictionary containing the book data.
    print(new_book)
    return {"message": "Book created successfully."}

@app.put("/books/{book_id}")
def put_update_book(book_id: int, updated_data: dict):
    # Here, `book_id` is the ID of the book to be updated, and `updated_data` is the new data for the book.
    print(f"Updating book with ID {book_id} to: {updated_data}")
    # Perform the update operation.
    return {"message": f"Book with ID {book_id} updated successfully."}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    # Here, `book_id` is the ID of the book to be deleted.
    print(f"Deleting book with ID {book_id}")
    # Perform the delete operation.
    return {"message": f"Book with ID {book_id} deleted successfully."}
