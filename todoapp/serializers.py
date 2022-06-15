from dataclasses import field
from rest_framework import serializers
from .models import *


class ToDoSerializers(serializers.ModelSerializer):
    # class Meta:
    #     model =ToDoList
    #     fields = ('Title')

    class Meta:
        model =ToDo
        fields = "__all__"