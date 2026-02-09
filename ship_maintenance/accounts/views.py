from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ProfileSerializer,RegisterUserSerializer,LoginSerializer
from .models import Profile
from django.contrib.auth.models import User

@api_view(['POST'])
def user_register(request):
    serializer = RegisterUserSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({
            "message":'Registered User successfully',
            "user_id":user.id,
            "username": user.username,
            "email":user.email,
        },status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 
    
@api_view(['POST'])
def user_login(request):
    serializer = LoginSerializer(data=request.data)

    if not serializer.is_valid():
        return Response({'error':"ENTER CORRECT EMAIL AND PASSWORD"},status=status.HTTP_400_BAD_REQUEST)
    
    user = serializer.validated_data['user']
    return Response({
        "user_id" :  user.id,
        "email":user.email,
        "role":Profile.role if Profile else None,
    },status=status.HTTP_200_OK)


def is_admin(user):
    try:
        return Profile.objects.get(user = user).role == 'ADMIN'
    except Profile.DoesNotExist:
        return False
    

