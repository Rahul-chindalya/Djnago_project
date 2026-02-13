from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes

from .serializer import ComponentSerializer
from .models import Component
from ships.permission import ISAdminOrEngineer


# Create your views here.
@api_view(['POST'])
@permission_classes([ISAdminOrEngineer])
def component_create(request):
    serializer = ComponentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([ISAdminOrEngineer])
# def components_list(request):
#     component = Component.objects.all()
#     serializer = ComponentSerializer(component)
#     return Response(serializer.data)

@api_view(['GET'])
@permission_classes([ISAdminOrEngineer])
def components_list(request):
    components = Component.objects.all()
    serializer = ComponentSerializer(components,many=True)

    result = []

    for sr in serializer.data:
        result.append({
            "id": sr['id'],
            "name": sr['name'],
            "serial_number": sr['serial_number'],
            "ship_name": sr['ship']
            
        })
    return Response(result)

@api_view(['GET'])
@permission_classes([ISAdminOrEngineer])
def components_detail(request,id):
    try:
        components = Component.objects.get(id=id)
    except Component.DoesNotExist:
        return Response({"ERROR":"INVALID DETAILS"})
    
    serilizer = ComponentSerializer(components)
    return Response(serilizer.data)


@api_view(['PUT'])
@permission_classes([ISAdminOrEngineer])
def components_update(request,id):
    try:
        component = Component.objects.get(id=id)
    except Component.DoesNotExist:
        return Response({"ERROR":"ENTER A VALID ID (ID DOES NOT EXISTS)"},status=status.HTTP_400_BAD_REQUEST)
    
    serializer = ComponentSerializer(component,data=request.data,partial =True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([ISAdminOrEngineer])
def component_delete(request,id):
    try:
        component = Component.objects.get(id=id)
    except Component.DoesNotExist:
        return Response({"ERROR":"ID DOEST NOT EXISTS"},status=status.HTTP_400_BAD_REQUEST)
    component.delete()
    return Response({"Message":"Deleted successfully!!",
                     "DATA":{
                        "name": component.name,
                        "serial_number": component.serial_number,
                        "ship_name": component.ship.name     
                     }},status=status.HTTP_200_OK)