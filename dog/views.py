from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Dog
from .serializers import DogSerializer
from rest_framework import status
import json
#from django.db.models import Q

# if we want to get dogs
# GET /dogs

# if we want to add dogs
# POST /dogs

# if we want to get a single dogs
# GET /dogs/:id

# if we want to update a dogs
# PUT /dogs/:id

# if we want to delete a dogs
# DELETE /dogs/:id


# safe=False allows us to give python data type to response

"""@api_view(['GET'])
def main(request):
    data = 'Welcome to TinDogs API developed by Zeyneb Besra Ozden'
    return Response(data)"""

@api_view(['GET'])
def get_dogs(request):

    dog_list = Dog.objects.all()
    serializer = DogSerializer(dog_list, many = True)
    #return Response(serializer.data, status=status.HTTP_200_OK, content_type='application/json')
    return JsonResponse(dog_list, safe=False)

    # Handle get requests

    # if request.method == 'GET':
    #     query = request.GET.get('query')

    #     if query == None:
    #         query = ''

    #     dogs=Dog.objects.filter(Q(name__icontains = query))
    #     serializer = DogSerializer(dogs, many=True)
    #     return Response(serializer.data)
    
    # if request.method == 'POST':

    #     dog=Dog.objects.create(
    #         name=request.data['name'],
    #     )
    #     serializer = DogSerializer(dogs, many=False)
    #     return Response(serializer.data)



@api_view(['POST'])
def add_dog(request):

    Dog.objects.create(
        name=request.data['name'],
    )
    return Response('added',status=status.HTTP_200_OK, content_type='application/json')
    

@api_view(['GET'])
def get_dog(request, id):
    
    dog = Dog.objects.get(id = id)
    serializer = DogSerializer(dog, many = False)
    return Response(serializer.data,status=status.HTTP_200_OK, content_type='application/json')

