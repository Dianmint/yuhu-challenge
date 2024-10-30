from rest_framework import serializers
from tasks.models import Task

READ_ONLY_FIELDS = ['id', 'completed_at', 'created_at', 'updated_at', 'done']

class TaskAPISerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = ['title', 'email', 'description'] + READ_ONLY_FIELDS
        read_only_fields = READ_ONLY_FIELDS
