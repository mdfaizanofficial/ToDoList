from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# CRUD Operations.

class ListToDo(generics.ListAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class DetailsToDo(generics.UpdateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class CreateToDo(generics.CreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers

class DeleteToDo(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializers



