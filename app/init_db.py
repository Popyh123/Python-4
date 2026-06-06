from db.db import engine, Base, get_db
from db import crud
from db import models

#Создание всех таблиц
Base.metadata.create_all(bind=engine)

db = next(get_db())

#Добавление категорий
category1 = crud.create_category(db, title="Фантастика")
category2 = crud.create_category(db, title="Программирование")

print(f"Созданы категории: {category1.title}, {category2.title}")

#Фантастика
book1 = crud.create_book(
    db=db,
    title="Дюна",
    description="Роман Фрэнка Герберта о пустынной планете Арракис",
    price=599.99,
    category_id=category1.id,
    url=""
)

book2 = crud.create_book(
    db=db,
    title="Основание",
    description="Роман Айзека Азимова о падении Галактической Империи",
    price=499.99,
    category_id=category1.id,
    url=""
)

#Программирование
book3 = crud.create_book(
    db=db,
    title="Изучаем Python",
    description="Полное руководство по программированию на Python",
    price=1299.99,
    category_id=category2.id,
    url=""
)

book4 = crud.create_book(
    db=db,
    title="Чистый код",
    description="Создание, анализ и рефакторинг кода",
    price=899.99,
    category_id=category2.id,
    url=""
)

print(f"Добавлены книги: {book1.title}, {book2.title}, {book3.title}, {book4.title}")
print("\nБаза данных успешно инициализирована!")