# from django.shortcuts import render
from .models import Dog
from .serializers import DogSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# safe=False allows us to give python data type to response

@api_view(['GET'])
def main(request):
    data = 'Welcome to TinDogs API developed by Zeyneb Besra Ozden'
    return Response(data)

@api_view(['GET'])
def get_dogs(request):

    dog_list = Dog.objects.all()
    serializer = DogSerializer(dog_list, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_dog(request, id):
    
    dog = Dog.objects.get(id = id)
    serializer = DogSerializer(dog, many = False)
    return Response(serializer.data)
