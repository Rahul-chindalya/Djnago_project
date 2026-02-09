# What serializer actually does:

# Validate data
# Create / update model
# Convert model → JSON
# “Serializers handle validation and object creation.
# Registration logic is placed inside the serializer’s create() method, while authentication is validated using authenticate() inside the login serializer. Views only manage request flow and responses.”

from rest_framework import serializers
from . models import Profile
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_no','role','address']

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True )

    class Meta:
        model = User
        fields = ['username','email','password']

    def create(self,validated_data):
        role = validated_data['role']
        user = User.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password']
        )
        Profile.objects.create(
                user=user,
                role=role,
            )
        return user
                                                                

# loginSerializer to Check authenticate user authorise

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password =serializers.CharField(write_only=True)

    def validate(self,data):
        user_obj = User.objects.filter(email=data['email']).first()

        if not user_obj:
            raise serializers.ValidationError("Invalid email or password")
        
        user = authenticate(username =user_obj.username, password = data['password'])

        if not user:
            raise serializers.ValidationError("Invalid email or password")
        
        data['user'] = user
        return data