from rest_framework import serializers
from .models import *

class ToDoSerializers(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('Id', 'Title', 'Description', 'Date', 'Complete')
