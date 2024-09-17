from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied

from .models import Tag, Task


# Fetch all tasks for the authenticated user
def get_tasks(request):
    return Task.objects.filter(owner=request.user)


# Fetch a single task by ID, and check if the owner matches the current user
def get_task_by_id(pk, user):
    task = get_object_or_404(Task, pk=pk)
    if task.owner != user:
        raise PermissionDenied("You do not have permission to access this task.")
    return task


# Fetch all tags for the authenticated user
def get_tags(request):
    return Tag.objects.filter(owner=request.user)


# Fetch a single tag by ID and ensure the current user is the owner
def get_tag_by_id(pk, user):
    tag = get_object_or_404(Tag, pk=pk)
    if tag.owner != user:
        raise PermissionDenied("You do not have permission to access this tag.")
    return tag
