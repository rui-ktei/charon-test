import socket

from fastapi import FastAPI

DATABASE_HOST = "localhost"
DATABASE_PORT = 5432
DATABASE_CONNECT_TIMEOUT = 5

app = FastAPI()


def open_database_channel() -> socket.socket:
    return socket.create_connection(
        (DATABASE_HOST, DATABASE_PORT), timeout=DATABASE_CONNECT_TIMEOUT
    )


database_channel = open_database_channel()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/db/health")
def database_health():
    return {"status": "ok", "peer": str(database_channel.getpeername())}
