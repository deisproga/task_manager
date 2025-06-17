Task Manager API — Django REST Framework

Проект таск-менеджера на Django и DRF  
Можно регаться, логиниться, создавать задачи, редачить, фильтровать, искать, удалять и отслеживать дедлайны

Установка и запуск

1. Клонируй репозиторий

   git clone <ссылка-на-репозиторий>  
   cd <папка-проекта>

2. Виртуальное окружение

   python -m venv venv  
   venv\Scripts\activate  (Windows)  
   source venv/bin/activate  (Linux/Mac)

3. Установка зависимостей

   pip install -r requirements.txt

4. Миграции и суперпользователь

   python manage.py migrate  
   python manage.py createsuperuser

5. Запуск сервера

   python manage.py runserver

Работа с API

1. Регистрация

   POST /api/register/

   {
       "username": "твой_ник",
       "email": "твоя_почта",
       "password": "твой_пароль"
   }

2. Получение токенов

   POST /api/token/

   {
       "username": "твой_ник",
       "password": "твой_пароль"
   }

   Ответ:

   {
       "access": "токен",
       "refresh": "токен"
   }

3. Добавь токен в заголовки

   Authorization: Bearer <access-токен>

4. Работа с задачами

   GET /api/tasks/ — список задач  
   POST /api/tasks/ — создать задачу  
   GET /api/tasks/<id>/ — получить одну  
   PUT /api/tasks/<id>/ — обновить  
   DELETE /api/tasks/<id>/ — удалить

   Пример задачи:

   {
       "title": "Название",
       "description": "Описание",
       "status": "new",
       "due_date": "2025-06-30",
       "tags": ["backend", "django"]
   }

   Фильтрация:

   /api/tasks/?status=new  
   /api/tasks/?ordering=due_date  
   /api/tasks/?search=работа


Docker способ

1. Собери образ

   docker build -t task_manager .

2. Запусти контейнер

   docker run -p 8000:8000 task_manager

Если используешь docker-compose:

   docker-compose up --build

3. Документация будет доступна на

   http://localhost:8000/api/

Если надо создать суперпользователя:

   docker exec -it <название_контейнера> python manage.py createsuperuser

Просрочка задачи считается автоматически если дедлайн прошёл а статус не done

Сделано для тестового задания