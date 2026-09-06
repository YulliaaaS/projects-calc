# Беремо офіційний легкий образ Python
FROM python:3.10-slim

# Вказуємо робочу папку всередині контейнера
WORKDIR /app

# Копіюємо ВСІ файли та папки з папки frontend (включаючи templates/)
COPY . .

# Встановлюємо потрібні бібліотеки
RUN pip install flask requests

# Відкриваємо порт 5000
EXPOSE 5000

# Команда для запуску додатка
CMD ["python", "main.py"]