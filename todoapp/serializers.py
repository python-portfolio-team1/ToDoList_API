from dataclasses import field
from rest_framework import serializers
from .models import *


class ToDoSerializers(serializers.ModelSerializer):
    class meta:
        model = ToDo
        fields = ('id', 'Title', 'Description', 'Date', 'Completed')