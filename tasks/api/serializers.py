from rest_framework import serializers
from tasks.models import Task

class TaskAPISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['title', 'email', 'description']
        read_only_fields = ['id', 'completed_at', 'created_at', 'updated_at']
