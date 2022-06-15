from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *



# CRUD Operations

class ListToDo(generics.ListAPIView):                    #Read
    Queryset = ToDo.objects.all()
    serializers_class = ToDoSerializers

class DetailToDo(generics.RetrieveUpdateAPIView):        #Update
    Queryset = ToDo.objects.all()
    serializers_class = ToDoSerializers

class CreateToDo(generics.CreateAPIView):                #Create
    Queryset = ToDo.objects.all()
    serializers_class = ToDoSerializers

class DeleteToDo(generics.DestroyAPIView):              #Delete
    Queryset = ToDo.objects.all()
    serializers_class = ToDoSerializers      