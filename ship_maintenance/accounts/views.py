from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .permissions import IsSuperUser
from .serializer import ProfileSerializer, RegisterUserSerializer, LoginSerializer
from .models import Profile


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
    
    profile = Profile.objects.filter(user=user).first()
    return Response({
        "user_id" :  user.id,
        "email":user.email,
        "role":profile.role if profile else None,
    },status=status.HTTP_200_OK)


# def is_admin(user):
#     if not user.is_authenticated:
#         return False
#     profile = Profile.objects.filter(user=user).first()
#     if not profile:
#         return False

#     return profile.role == 'ADMIN'
    
@api_view(['GET'])
@permission_classes([IsSuperUser])
def users_list(request):

    # check admin role

    profiles = Profile.objects.select_related('user').all()
    result = []

    for profile in profiles:

        result.append({
            "id": profile.user.id,
            "username": profile.user.username,
            "email": profile.user.email,
            "role": profile.role 
        })

    return Response(result, status=status.HTTP_200_OK)



@api_view(['GET'])
@permission_classes([IsSuperUser])
def user_detail(request,id):

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error":'USER DOES NOTEXISTS'},status=status.HTTP_404_NOT_FOUND)

    profile = Profile.objects.filter(user=user).first()
    return Response({
        "id": user.id,
        "username": user.username, 
        "email": user.email,
        "role": profile.role if profile else None,
        "phone_no":profile.phone_no if profile else None ,
        "address":profile.address if profile else None
    },status= status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsSuperUser])
def user_update(request,id):

    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    profile =Profile.objects.filter(user=user).first()
    #update user
    user.username = request.data.get('username',user.username)
    user.email = request.data.get('email',user.email)
    user.save()
    if profile:
        profile.role = request.data.get('role', profile.role)
        profile.phone_no = request.data.get('phone_no', profile.phone_no)
        profile.address = request.data.get('address', profile.address)
        profile.save()

    return Response({"message": "User updated successfully","data": {
        "id": user.id,"username": user.username,"email": user.email,"role": profile.role if profile else None,
        "phone_no": profile.phone_no if profile else None, "address": profile.address if profile else None}
        }, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsSuperUser])
def user_delete(request,id):
    try:
        user = User.objects .get(id=id)
    except User.DoesNotExist:
        return Response({'ERROR':"User not found"},status=status.HTTP_404_NOT_FOUND)
    
    user.delete()

    return Response({'message':'DELETED USER SUCCESSFULLY','Data':{
        "id":user.id,
        "username":user.username,
        "email":user.email,
        "role":Profile.role if Profile else None,
        "phone_no":Profile.phone_no if Profile else None,
        "address":Profile.address if Profile else None,
    }},status=status.HTTP_200_OK)
