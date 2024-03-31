from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo


class TodoView(viewsets.ModelViewSet):
    #instance of the 'TodoView' class will use 'TodoSerializer' to
    # serialize and deseriallize data when performing crud operations
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()