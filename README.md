## Установка и запуск

1. Клонирование репозитория
git clone https://github.com/Popyh123/Python-4.git
cd Python-4

2. Активация виртуального окружения
source venv/bin/activate

3. Установка зависимостей
pip install -r requirements.txt

4. Настройка базы данных
Убедитесь, что PostgreSQL запущен в WSL и создана база данных octagon_db с пользователем octagon.
Файл .env должен содержать:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

5. Инициализация базы данных
python app/init_db.py

6. Запуск API
uvicorn app.main:app --reload

7. Просмотр документации
Откройте в браузере:
Swagger UI: http://127.0.0.1:8000/docs


API Endpoints:
### Категории
- `GET /categories/` - получить все категории
- `POST /categories/` - создать категорию
- `GET /categories/{id}` - получить категорию по ID
- `PUT /categories/{id}` - обновить категорию
- `DELETE /categories/{id}` - удалить категорию

### Книги
- `GET /books/` - получить все книги
- `POST /books/` - создать книгу
- `GET /books/{id}` - получить книгу по ID
- `PUT /books/{id}` - обновить книгу
- `DELETE /books/{id}` - удалить книгу