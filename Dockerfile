# Используем официальный Python-образ
FROM python:3.9-slim
# Указываем рабочую директорию внутри контейнера
WORKDIR /app
# Копируем файл зависимостей и устанавливаем их
COPY requirements.txt ./ RUN pip install --no-cache-dir -r requirements.txt
# Копируем всё остальное
COPY . .
# Команда по умолчанию для запуска приложения
CMD ["python", "app.py"]# Базовый образ с Python FROM python:3.10-slim
# Установка зависимостей системы
RUN apt-get update && apt-get install -y --no-install-recommends \ libpq-dev gcc \ && rm -rf /var/lib/apt/lists/*
# Устанавливаем рабочую директорию
WORKDIR /app
# Копируем файлы
COPY requirements.txt /app/
# Установка зависимостей Python
RUN pip install --no-cache-dir -r requirements.txt
# Копируем весь проект
COPY . /app/
# Установка переменных окружения
ENV PYTHONDONTWRITEBYTECODE 1 ENV PYTHONUNBUFFERED 1
# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
