from fastapi import FastAPI

app = FastAPI()

SERVICE_VERSION = "1.1.0"


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "healthy", "version": SERVICE_VERSION}
