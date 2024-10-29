from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from tasks.models import Task
from .serializers import TaskAPISerializer


class TaskAPIViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskAPISerializer
    
    @action(detail=True, methods=['patch'], url_path='complete')
    def mark_as_complete(self, request, pk=None):
        """
        Endpoint to mark task as completed
        """
        task = self.get_object()
        task.done = True
        task.completed_at = timezone.now()
        task.save()
        
        serializer = self.get_serializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    