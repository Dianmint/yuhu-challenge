from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',             
        'email',             
        'created_at',       
    )
    search_fields = ('title', 'email')
    ordering = ('-created_at',)  