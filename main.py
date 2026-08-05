from fastapi import FastAPI

app = FastAPI()

DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 50


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/items")
def list_items(limit: int = DEFAULT_PAGE_SIZE):
    page_size = min(limit, MAX_PAGE_SIZE)
    return {"items": [], "limit": page_size}
