from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db.db import engine, Base, get_db
from app.api import books, categories


app = FastAPI(
    title="Book Store API",
    description="API для управления книгами и категориями",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(categories.router)
app.include_router(books.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to Book Store API",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "API is running"
    }