from rest_framework import serializers
from .models import *

class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = todos
        fields = ['title', 'name']