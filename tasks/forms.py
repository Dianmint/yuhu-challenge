from django import forms
from tasks.models import Task  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'email', 'description', 'expirate_at']
        widgets = {
            'expirate_at': forms.DateInput(attrs={'type': 'date'}),
        }
