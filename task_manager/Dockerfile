FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Обновляем pip и ставим зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Открываем порт
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]