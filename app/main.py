from db.db import get_db
from db import crud

# Получаем сессию БД
db = next(get_db())

print("БАЗА ДАННЫХ КНИЖНОГО МАГАЗИНА")

#Вывод категорий
print("\n📚 КАТЕГОРИИ:")
print("-" * 60)
categories = crud.get_categories(db)
for category in categories:
    print(f"ID: {category.id} | Название: {category.title}")

#Вывод книг
print("\n📖 КНИГИ:")
print("-" * 60)
books = crud.get_books(db)
for book in books:
    category = crud.get_category_by_id(db, book.category_id)
    print(f"ID: {book.id}")
    print(f"Название: {book.title}")
    print(f"Описание: {book.description}")
    print(f"Цена: {book.price} ₽")
    print(f"Категория: {category.title if category else 'N/A'}")
    print("-" * 60)

print("\n✅ Данные успешно получены из базы данных!")