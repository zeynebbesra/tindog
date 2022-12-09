from rest_framework import serializers
from .models import Dog

class DogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ('dog_id', 'name', 'breed','gender', 'img', 'age')
