from rest_framework import serializers
from . models import Profile
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_no','role','address']


# loginSerializer to Check authenticate user authorise

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password =serializers.CharField(write_only=True)
    