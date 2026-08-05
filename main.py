from fastapi import FastAPI

app = FastAPI()

DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 50

HEALTH_STATUS = "healthy"


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": HEALTH_STATUS}


@app.get("/items/count")
def count_items(per_page: int = DEFAULT_PAGE_SIZE):
    return {"count": 0, "per_page": per_page}


@app.get("/items")
def list_items(limit: int = DEFAULT_PAGE_SIZE, offset: int = 0):
    page_size = min(limit, MAX_PAGE_SIZE)
    start = max(offset, 0)
    return {"items": [], "limit": page_size, "offset": start}


@app.get("/items/search")
def search_items(query: str = "", limit: int = DEFAULT_PAGE_SIZE):
    page_size = min(limit, MAX_PAGE_SIZE)
    return {"items": [], "query": query, "limit": page_size}


@app.get("/items/page")
def page_items(page: int = 1, size: int = DEFAULT_PAGE_SIZE):
    page_size = min(size, MAX_PAGE_SIZE)
    return {"items": [], "page": page, "size": page_size}


@app.get("/items/window")
def window_items(start: int = 0, size: int = DEFAULT_PAGE_SIZE):
    page_size = min(size, MAX_PAGE_SIZE)
    return {"items": [], "start": max(start, 0), "size": page_size}
