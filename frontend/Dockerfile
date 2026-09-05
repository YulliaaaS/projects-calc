# Беремо офіційний легкий образ Python
FROM python:3.10-slim

# Вказуємо робочу папку всередині контейнера
WORKDIR /app

# Копіюємо файл коду в контейнер
COPY main.py .

# Встановлюємо потрібні бібліотеки
RUN pip install flask requests

# Відкриваємо порт 5000
EXPOSE 5000

# Команда для запуску додатка
CMD ["python", "main.py"]