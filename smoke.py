from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
assert client.get("/").json() == {"message": "Hello, World!"}
assert client.get("/health").json() == {"status": "healthy"}
assert client.get("/items/count").json() == {"count": 0, "per_page": 10}
