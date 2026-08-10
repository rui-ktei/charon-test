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
    return {"count": 0, "per_page": min(per_page, MAX_PAGE_SIZE)}
