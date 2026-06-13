from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from app.db.db import get_db
from app.db import crud
from app.db import models
from app.schemas import Book, BookCreate

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/", response_model=List[Book])
def get_books(
    category_id: Optional[int] = Query(None, description="Фильтр по ID категории"),
    db: Session = Depends(get_db)
):
    """Получить все книги (можно фильтровать по category_id)"""
    if category_id:
        category = crud.get_category_by_id(db, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Категория не найдена")
        return db.query(models.Book).filter(models.Book.category_id == category_id).all()
    return crud.get_books(db)

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Получить книгу по ID"""
    book = crud.get_book_by_id(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return book

@router.post("/", response_model=Book, status_code=201)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    """Создать новую книгу"""
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    return crud.create_book(
        db=db,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )

@router.put("/{book_id}", response_model=Book)
def update_book(
    book_id: int,
    book: BookCreate,
    db: Session = Depends(get_db)
):
    """Обновить книгу"""
    db_book = crud.get_book_by_id(db, book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    
    category = crud.get_category_by_id(db, book.category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Категория не найдена")
    
    return crud.update_book(
        db=db,
        book_id=book_id,
        title=book.title,
        description=book.description,
        price=book.price,
        category_id=book.category_id,
        url=book.url
    )

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    """Удалить книгу"""
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    return {"message": "Книга успешно удалена"}