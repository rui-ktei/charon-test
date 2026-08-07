from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
assert client.get("/").json() == {"message": "Hello, World!"}
assert client.get("/health").json() == {"status": "healthy"}
assert client.get("/items/window").json() == {
    "items": [],
    "start": 0,
    "size": 10,
    "total": 0,
    "has_more": False,
    "page": 1,
}
