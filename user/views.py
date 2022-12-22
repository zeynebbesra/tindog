from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import User
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

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

#user'ı id'ye göre veriyor

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




