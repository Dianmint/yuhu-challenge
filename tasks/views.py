from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils import timezone

from .models import Task
from .forms import TaskForm

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('task_list')
    
    
class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_tasks'] = Task.objects.filter(done=False)
        context['completed_tasks'] = Task.objects.filter(done=True)
        return context
    

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'update_task.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        return super().form_valid(form)
    

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('task_list')
    

class MarkTaskAsDoneView(UpdateView):
    model = Task
    fields = []
    template_name = 'tasks/mark_task_as_done.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        task = form.instance
        task.done = True
        task.completed_at = timezone.now()
        task.save()
        return redirect(self.success_url)