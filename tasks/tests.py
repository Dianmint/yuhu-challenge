from rest_framework import status
from rest_framework.test import APITestCase

from django.db.models.signals import post_save, post_delete
from django.urls import reverse

from .models import Task
from .signals import send_update_notification, send_task_deletion_notification

class TaskAPITestCase(APITestCase):

    @classmethod
    def setUpTestData(cls):
        post_save.disconnect(send_update_notification, sender=Task)
        post_delete.disconnect(send_task_deletion_notification, sender=Task)
        
        cls.task = Task.objects.create(
            title="Test Task",
            email="test@example.com",
            description="A test task"
        )
        
        cls.task_url = reverse('task-detail', kwargs={'pk': cls.task.id})  
        cls.tasks_list_url = reverse('task-list')
        cls.complete_url = reverse('task-mark-as-complete', kwargs={'pk': cls.task.id})
        print(cls.task_url)
        print(cls.tasks_list_url)
        print(cls.complete_url)


    def test_list_tasks(self):

        response = self.client.get(self.tasks_list_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)

    def test_create_task(self):

        data = {
            "title": "New Task",
            "email": "new@example.com",
            "description": "A new task"
        }
        
        response = self.client.post(self.tasks_list_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['email'], data['email'])

    def test_get_task_detail(self):
        
        response = self.client.get(self.task_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)
        self.assertEqual(response.data['description'], self.task.description)

    def test_update_task(self):
        
        data = {
            "title": "Updated Task",
            "email": "updated@example.com",
            "description": "An updated task"
        }
        response = self.client.put(self.task_url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['email'], data['email'])

    def test_mark_task_as_complete(self):
        
        response = self.client.patch(self.complete_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertTrue(self.task.done)
        self.assertIsNotNone(self.task.completed_at)

    def test_delete_task(self):
        
        response = self.client.delete(self.task_url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Task.objects.filter(id=self.task.id).exists())
