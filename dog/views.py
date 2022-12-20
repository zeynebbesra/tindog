from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dog
from .serializers import DogSerializer
from rest_framework import status



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

#dogs listesini veriyor
@api_view(['GET'])
def get_dogs(request):           

    dog_list = Dog.objects.all()
    serializer = DogSerializer(dog_list, many = True)
    Response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return Response(serializer.data, status=status.HTTP_200_OK, )

#dogs listesine dog ekliyor
@api_view(['POST'])
def add_dog(request):

    Dog.objects.create(
        name=request.data['name'],
    )
    Response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return Response('added',status=status.HTTP_200_OK,)
    
#dog'u id'ye göre veriyor
@api_view(['GET'])
def get_dog(request, id):
    
    dog = Dog.objects.get(id = id)
    serializer = DogSerializer(dog, many = False)
    Response["Access-Control-Allow-Origin"] = "http://localhost:3000"
    return Response(serializer.data,status=status.HTTP_200_OK)

