from django.urls import path

from .views import (
    TagDetailAPIView,
    TagListCreateAPIView,
    TaskDetailAPIView,
    TaskListCreateAPIView,
)

app_name = "tasks"
urlpatterns = [
    path("tasks/", TaskListCreateAPIView.as_view(), name="task-list-create"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail"),
    path("tags/", TagListCreateAPIView.as_view(), name="tag-list-create"),
    path("tags/<int:pk>/", TagDetailAPIView.as_view(), name="tag-detail"),
]
