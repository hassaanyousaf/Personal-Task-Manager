# Task Manager

Full-stack task management application built with Django REST Framework with JWT authentication. Features complete CRUD operations, inline editing, and responsive design.

## Features
- JWT-based user authentication (login/register)
- Complete CRUD operations for tasks
- Inline title editing and quick complete toggle
- Task statistics dashboard
- RESTful API with ModelViewSet

## How It Works

### 1. Authentication Flow
- User visits /register/ → Creates account via POST /api/register/
- Redirects to /login/ → POST /api/login/ returns JWT access/refresh tokens
- Tokens stored in localStorage → All API calls use "Authorization: Bearer {token}"
- Protected routes check IsAuthenticated permission

### 2. Task Management Flow
Dashboard (/dashboard/)
├── Create task → POST /api/tasks/ {title: "Buy groceries"}
└── View Tasks → GET /tasks/

Tasks Page (/tasks/)
- List all tasks → GET /api/tasks/
-  Inline edit title → PATCH /api/tasks/{id}/ {title: "new title"}
- Toggle complete → PATCH /api/tasks/{id}/ {completed: true}
- Delete → DELETE /api/tasks/{id}/
- Edit → /update/{id}/ (full form)

Update Page (/update/{id}/)
- Load task → GET /api/tasks/{id}/
- Full update → PUT /api/tasks/{id}/ {title, description, completed}

## Tech Stack
- Backend: Django 5.0, Django REST Framework 3.15, SimpleJWT
- Frontend: Vanilla HTML/CSS/JavaScript
- Database: SQLite
- Styling: Custom CSS with Segoe UI font

## Quick Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
