from rest_framework.serializers import ModelSerializer
from .models import Dog
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields='_all_'

class DogSerializer(ModelSerializer):
    class Meta:
        model=Dog
        fields='__all__'
