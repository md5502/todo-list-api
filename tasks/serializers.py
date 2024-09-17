from rest_framework import serializers

from .models import Tag, Task


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "owner",
            "description",
            "status",
            "hours",
            "planned_start_date",
            "planned_end_date",
            "actual_start_date",
            "actual_end_date",
            "content",
            "tags",
            "sub_tasks",
        ]
