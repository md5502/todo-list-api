from django.contrib import admin

from .models import Tag, Task

# Custom admin for BaseUser


# Custom admin for Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "owner",
        "status",
        "planned_start_date",
        "planned_end_date",
        "actual_start_date",
        "actual_end_date",
    )
    list_filter = ("status", "planned_start_date", "actual_start_date")
    search_fields = ("title", "description", "owner__username")
    autocomplete_fields = ["owner", "tags", "sub_tasks"]
    date_hierarchy = "planned_start_date"
    ordering = ["planned_start_date"]


# Custom admin for Tag
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_by")
    search_fields = ("name", "created_by")
