from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, RegisterView, ProtectedView
from django.urls import path


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='api-register'),
    path('protected/', ProtectedView.as_view(), name='protected'),
] + router.urls
