# Проект Collect


## Требования

- Docker
- Docker Compose

## Запуск проекта

1. Создать .env и добавить переменные окружение из примера [.env.example](.env.example)


2. Соберите и запустите контейнеры:

```bash
  docker-compose up --build
```

3. В папке проекта применить миграции:

```bash
  docker compose exec backend_local python manage.py migrate
```

4. Для наполнение базы данных выполнить команду:

```bash
  docker compose exec backend_local python manage.py populate_db
```

5. Проект будет доступен по адресу:
http://localhost:8000
