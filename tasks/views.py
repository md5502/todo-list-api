from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import get_tag_by_id, get_tags, get_task_by_id, get_tasks
from .serializers import TagSerializer, TaskSerializer
from .services import create_tag, create_task, delete_tag, delete_task, update_tag, update_task


# Task List/Create API View
class TaskListCreateAPIView(APIView):
    def get(self, request):
        tasks = get_tasks(request)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = create_task(serializer.validated_data, request.user)
        return Response(TaskSerializer(task).data, status=status.HTTP_201_CREATED)


# Task Detail API View
class TaskDetailAPIView(APIView):
    def get(self, request, pk):
        task = get_task_by_id(pk, request.user)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = get_task_by_id(pk, request.user)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            updated_task = update_task(task, serializer.validated_data)
            return Response(TaskSerializer(updated_task).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = get_task_by_id(pk, request.user)
        delete_task(task)
        return Response(status=status.HTTP_204_NO_CONTENT)


# Tag List/Create API View
class TagListCreateAPIView(APIView):
    def get(self, request):
        tags = get_tags(request)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tag = create_tag(serializer.validated_data, request.user)
        return Response(TagSerializer(tag).data, status=status.HTTP_201_CREATED)


# Tag Detail API View
class TagDetailAPIView(APIView):
    def get(self, request, pk):
        tag = get_tag_by_id(pk, request.user)
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    def put(self, request, pk):
        tag = get_tag_by_id(pk, request.user)
        serializer = TagSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            updated_tag = update_tag(tag, serializer.validated_data)
            return Response(TagSerializer(updated_tag).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tag = get_tag_by_id(pk, request.user)
        delete_tag(tag)
        return Response(status=status.HTTP_204_NO_CONTENT)
