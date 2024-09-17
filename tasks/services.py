from .models import Tag, Task


# Create a new task
def create_task(data, user):
    task = Task(**data, owner=user)
    task.save()
    return task


# Update a task
def update_task(task, data):
    for key, value in data.items():
        setattr(task, key, value)
    task.save()
    return task


# Delete a task
def delete_task(task):
    task.delete()


# Create a new tag
def create_tag(data, user):
    tag = Tag(**data, created_by=user)
    tag.save()
    return tag


# Update a tag
def update_tag(tag, data):
    for key, value in data.items():
        setattr(tag, key, value)
    tag.save()
    return tag


# Delete a tag
def delete_tag(tag):
    tag.delete()
