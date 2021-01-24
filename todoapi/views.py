from uuid import uuid4

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todoapi.models import ToDo
from todoapi.serializers import ToDoSerializer
from rest_framework import permissions


class ToDoList(ListCreateAPIView):
    """
    Methods on For ToDo
    """

    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, id=uuid4())

    def get_queryset(self):
        print(self.request.user)
        return ToDo.objects.all().filter(owner=self.request.user)


class ToDoDetailView(RetrieveUpdateDestroyAPIView):
    """
    Methods on For ToDo
    """

    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    lookup_field = "id"

    def get_queryset(self):
        return ToDo.objects.all().filter(owner=self.request.user)
