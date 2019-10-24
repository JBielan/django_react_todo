from rest_framework import routers
from .api import ToDoViewSet

router = routers.DefaultRouter()
router.register('', ToDoViewSet, 'tasks')

urlpatterns = router.urls
