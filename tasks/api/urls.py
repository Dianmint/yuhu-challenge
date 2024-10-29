from rest_framework.routers import DefaultRouter
from .views import TaskAPIViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'tasks', TaskAPIViewSet)

urlpatterns = [
    path('', include(router.urls)),
]