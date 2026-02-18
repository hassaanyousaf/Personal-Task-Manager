from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.shortcuts import render



class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer
 
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": f"Hello {request.user.username}, you are authenticated!"
        })    


def login_page(request):
    return render(request, "login.html")

def register_page(request):
    return render(request, "register.html")

def dashboard_page(request):
    return render(request, "dashboard.html")

def tasks_page(request):
    return render(request, 'tasks.html')
def update_task_page(request, pk):
    return render(request, 'update.html', {'task_id': pk})



