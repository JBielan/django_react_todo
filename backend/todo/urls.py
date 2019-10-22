from rest_framework import routers
from .api import ToDoViewSet

router = routers.DefaultRouter()
router.register('api/tasks', ToDoViewSet, 'tasks')

urlpatterns = router.urls
