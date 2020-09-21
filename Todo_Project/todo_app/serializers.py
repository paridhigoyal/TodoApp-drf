from rest_framework import serializers;
from .models import *



class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ('id', 'created_at')
        ordering = ['-created_at']