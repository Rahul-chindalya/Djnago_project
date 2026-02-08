from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from .models import Profile
from .serializer import LoginSerializer,UserSerializer
from django.contrib.auth import authenticate

# Create your views here.

@api_view(['POST'])
def login(request):
    serializer = LoginSerializer(data=request.data)

    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error':'Emial ID Does Not Exists '},status=status.HTTP_404_NOT_FOUND)
        
        user = authenticate(request,username=User.username,password=password)

        if not user:
            return Response({'error':'Email or Password dose not match'},status=status.HTTP_400_BAD_REQUEST)
        
        profile = Profile.objects.filter(user=user).first()#is used to stop crashing

                        # Object MUST exist          --->	     get()
                        # Object may or may not exist  --->   first()
        return Response({
            "user_id":User.id,
            "email": User.email,
            "role": profile.role,
            "phone_no": profile.phone_no,
            "address": profile.address
        })
    else:
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

def is_admin(user_id):
    profile = Profile.objects.filter(user_id=user_id).first()
    return profile and profile.role == "ADMIN"

@api_view(['POST'])
def create_user(request):
    admin_user_id = request.data.get('admin_user_id')

    if not is_admin(admin_user_id):
        return Response({"error": "Admin only"}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(request,data=request.data)

    if serializer.is_vaild():

        data = serializer.validated_data

        User.objects.create(
            username=data['password'],
            email=data['email'],
            password=data['password'],      
        )

        Profile.objects.create(
            phone_no = data['phone_no'],
            role = data['role'],
            address = data.get('address'),
            address = data.get('address'),
        )
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def list_user(request):
    # user = User.objects.all()
    profile = Profile.objects.select_related('user').all()
    serializer = UserSerializer(profile,many = True)
    return Response(serializer.data,status=status.HTTP_200_OK)



@api_view(['GET'])
def user_detail(request, user_id):
    admin_user_id = request.query_params.get('admin_user_id')

    if not Profile.objects.filter(user_id=admin_user_id, role="ADMIN").exists():
        return Response({"error": "Only admin can view user details"}, status=403)

    try:
        profile = Profile.objects.select_related('user').get(user_id=user_id)
        user = profile.user
    except Profile.DoesNotExist:
        return Response({"error": "User not found"}, status=404)

    return Response({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": profile.role,
        "phone": profile.phone,
        "address": profile.address
    }, status=200)

