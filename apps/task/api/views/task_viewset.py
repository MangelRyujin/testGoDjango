from rest_framework import viewsets
from apps.task.models import Task
from apps.task.api.serializers.task_serializer import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter,SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.pagination.pagination import TaskPagination
from django.contrib.auth.models import User

from utils.send_email.send_email import send_email_task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend,OrderingFilter,SearchFilter]
    filterset_fields = {
            'title': ['contains'],
            'state': ['exact'],
            'created_date_time': ['exact'],
        }
    search_fields = ['title', 'description','state']
    
    def perform_update(self, serializer):
        instance = serializer.save()
        for user in User.objects.all():
            send_email_task(instance, user.email)