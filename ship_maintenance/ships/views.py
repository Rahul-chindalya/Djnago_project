from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from .serializer import ShipSerializer
from .models import Ship
from .permission import ISAdminOrEngineer

# Create your views here.

@api_view(['POST'])
@permission_classes([ISAdminOrEngineer])
def ship_create(request):

    serializer = ShipSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def ship_list(request):
    ship = Ship.objects.all()
    serializer = ShipSerializer(ship,many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([ISAdminOrEngineer])
def ship_detail(request,id):
    try:
        ship = Ship.objects.get(id=id)
    except Ship.DoesNotExist:
        return Response({"ERROR":"ENTER THE VALID ID (ID Does NOt Exixts!!)"})
    
    serializer = ShipSerializer(ship)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([ISAdminOrEngineer])
def ship_update(request,id):
    try:
        ship = Ship.objects.get(id=id)
    except Ship.DoesNotExist:
        return Response({"ERROR":'ENTER A VALID ID'})
    
    serializer = ShipSerializer(ship,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([ISAdminOrEngineer])
def ship_delete(request,id):
    try:
        ship = Ship.objects.get(id=id)
    except Ship.DoesNotExist:
        return Response({"ERROR":'ID IS INVALID'})
    ship.delete()
    return Response({"MESSAGE":"DELETED USER SUCCESSFUL",
                     "DATA":{
                         ship.id,
                         ship.name,
                         ship.imo_number,
                         ship.flag,
                         ship.status,
                     }},status=status.HTTP_200_OK)