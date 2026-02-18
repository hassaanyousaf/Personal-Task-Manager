from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView, ProtectedView
from django.urls import path
from .views import login_page, register_page, dashboard_page, tasks_page, update_task_page

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register-page'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('tasks/', tasks_page, name='tasks-page'),
    path("update/<int:pk>/", update_task_page, name="update_page"),

] + router.urls
