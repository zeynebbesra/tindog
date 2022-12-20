from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework import status
# Create your views here.

#users listesini veriyor
@api_view(['GET'])
def get_users(request):
    user_list = User.objects.all()
    serializer = UserSerializer(user_list, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK,)

#users listesine user ekliyor
"""@api_view(['POST'])
def add_user(request):
    User.objects.create(
        first_name = request.data['first_name']
    )
    return Response('added', status=status.HTTP_200_OK,)"""

#user'ı id'ye göre veriyor
@api_view(['GET'])
def get_user(request, id):
    user=User.objects.get(id = id)
    serializer = UserSerializer(user, many = False)
    return Response(serializer.data, status=status.HTTP_200_OK,)




