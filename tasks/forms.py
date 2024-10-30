from django import forms
from tasks.models import Task  

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'email', 'description', 'expirate_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'expirate_at': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
