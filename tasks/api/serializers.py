from rest_framework import serializers
from tasks.models import Task

class TaskAPISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['id', 'title', 'email', 'description', 'created_at', 'updated_at']
        read_only_fields = ['completed_at']
