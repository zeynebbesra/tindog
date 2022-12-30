from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from .models import Dog
from .serializers import DogSerializer
from rest_framework import status
from rest_framework.views import APIView


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
    return Response(serializer.data, status=status.HTTP_200_OK, )

#dogs listesine dog ekliyor
@api_view(['POST'])
def add_dog(request):

    Dog.objects.create(
        name=request.data['name'],
    )
    return Response('added',status=status.HTTP_200_OK,)
    
#dog'u id'ye göre veriyor

"""@api_view(['GET','PUT','DELETE'])
def get_dog(request, id):
    dog = Dog.objects.get(id = id)
    if request.method == 'GET':
        serializer = DogSerializer(dog, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        dog.age = request.data['age']
        dog.img = request.data['img']

        dog.save()
        serializer = DogSerializer(dog, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        dog.delete()
        return Response("dog was deleted") """



class DogDetails(APIView):

    def get_object(self, id):
        try:
            return Dog.objects.get(id = id)
        except Dog.DoesNotExist:
            raise JsonResponse('Dog does not exist')

    def get(self, request, id):
        dog = self.get_object(id)
        serializer = DogSerializer(dog, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request, id):
        dog = self.get_object(id)
        dog.age = request.data['age']
        dog.img = request.data['img']
        serializer = DogSerializer(dog, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        dog = self.get_object(id)
        dog.delete()
        return Response("dog was deleted")


#users listesini veriyor
@api_view(['GET'])
def get_users(request):
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK,)


#users listesine user ekliyor
@api_view(['POST'])
def add_user(request):
    User.objects.create(
        first_name = request.data['first_name']
    )
    return Response('added', status=status.HTTP_200_OK,)

"""@api_view(['GET'])
def get_user(request, id):
    user=User.objects.get(id = id)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data, status=status.HTTP_200_OK,)"""



class UserDetails(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id = id)
        except User.DoesNotExist:
            raise JsonResponse('User does not exist')

    def get(self, request, id):
        user = self.get_object(id)
        serializer = UserSerializer(user, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request, id):
        user = self.get_object(id)
        user.email = request.data['email']
        user.age = request.data['email']
        user.city = request.data['email']
        user.password = request.data['password']
        user.img = request.data['img']
        user.bio = request.data['bio']
        serializer = UserSerializer(user, many = False)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self, request, id):
        dog = self.get_object(id)
        dog.delete()
        return Response("user was deleted")




    

