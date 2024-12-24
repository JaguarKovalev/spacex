# Используем официальный образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app/

# Устанавливаем Poetry через pip
RUN pip install poetry

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-dev

# Открываем порт 8000 для доступа
EXPOSE 8000

# Запускаем сервер Django
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
