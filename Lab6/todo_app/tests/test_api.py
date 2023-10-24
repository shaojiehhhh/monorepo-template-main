from fastapi.testclient import TestClient
from todo_app.src.main import app

client = TestClient(app)

def test_get_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World!"}

def test_get_api_with_path_param():
    path_param = "John"
    response = client.get(f"/books/{path_param}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {path_param}"}

def test_get_api_with_query_param():
    title = "Python"
    response = client.get(f"/books/?title={title}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {title}"}

def test_get_api_with_path_and_query_params():
    path_param = "John"
    title = "Python"
    response = client.get(f"/books/{path_param}/?title={title}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello {path_param}, {title}"}

def test_post_create_book():
    new_book = {"title": "New Book", "author": "Author"}
    response = client.post("/books/create_book", json=new_book)
    assert response.status_code == 200
    assert response.json() == {"message": "Book created successfully."}

def test_put_update_book():
    book_id = 1
    updated_data = {"title": "Updated Book", "author": "New Author"}
    response = client.put(f"/books/{book_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json() == {"message": f"Book with ID {book_id} updated successfully."}

def test_delete_book():
    book_id = 1
    response = client.delete(f"/books/{book_id}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Book with ID {book_id} deleted successfully."}
