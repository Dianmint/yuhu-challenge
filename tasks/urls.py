from django.urls import path
from .views import TaskCreateView, TaskListView, TaskUpdateView, TaskDeleteView, MarkTaskAsDoneView

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create-task/', TaskCreateView.as_view(), name='create_task'),
    path('<uuid:pk>/edit/', TaskUpdateView.as_view(), name='update_task'),
    path('<uuid:pk>/delete/', TaskDeleteView.as_view(), name='delete_task'),
    path('tasks/<uuid:pk>/complete/', MarkTaskAsDoneView.as_view(), name='mark_task_as_done'),
]