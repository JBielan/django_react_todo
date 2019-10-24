from django.urls import path, include

urlpatterns = [
    path('api/tasks/', include('todo.urls')),
]
