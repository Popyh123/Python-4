from sqlalchemy.orm import Session
from . import models

#Category CRUD
def create_category(db: Session, title: str):
    """Создать категорию"""
    db_category = models.Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def get_categories(db: Session):
    """Получить все категории"""
    return db.query(models.Category).all()

def get_category_by_id(db: Session, category_id: int):
    """Получить категорию по ID"""
    return db.query(models.Category).filter(models.Category.id == category_id).first()


#Book CRUD
def create_book(db: Session, title: str, description: str, price: float, category_id: int, url: str = None):
    """Создать книгу"""
    db_book = models.Book(
        title=title,
        description=description,
        price=price,
        category_id=category_id,
        url=url
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    """Получить все книги"""
    return db.query(models.Book).all()

def get_book_by_id(db: Session, book_id: int):
    """Получить книгу по ID"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()

def update_book(db: Session, book_id: int, title: str = None, description: str = None, 
                price: float = None, url: str = None):
    """Обновить книгу"""
    db_book = get_book_by_id(db, book_id)
    if db_book:
        if title:
            db_book.title = title
        if description:
            db_book.description = description
        if price:
            db_book.price = price
        if url:
            db_book.url = url
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    """Удалить книгу"""
    db_book = get_book_by_id(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False