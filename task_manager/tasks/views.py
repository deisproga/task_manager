from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date
import logging

logger = logging.getLogger(__name__)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['status']
    ordering_fields = ['due_date']
    search_fields = ['title']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        if task.due_date < date.today() and task.status != 'done':
            logger.warning(f"Task '{task.title}' is overdue!")
