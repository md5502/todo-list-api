from django.db import models

from common.models import BaseModel
from users.models import BaseUser


class Task(BaseModel):
    STATUS_CHOICES = (
        ("not_started", "Not Started"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("on_hold", "On Hold"),
        ("cancelled", "Cancelled"),
    )
    title = models.CharField(max_length=120)
    owner = models.ForeignKey(BaseUser, on_delete=models.CASCADE, related_name="tasks")
    description = models.CharField(max_length=400, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES[0][0],
    )
    hours = models.FloatField(default=0)
    planned_start_date = models.DateTimeField(null=True, blank=True)
    planned_end_date = models.DateTimeField(null=True, blank=True)
    actual_start_date = models.DateTimeField(null=True, blank=True)
    actual_end_date = models.DateTimeField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", related_name="tasks", blank=True)
    sub_tasks = models.ManyToManyField("self", blank=True)

    def __str__(self) -> str:
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
