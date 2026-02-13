from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from .serializer import CalendarJobSerializer
from jobs.models import MaintainenceJobs
from ships.permission import ISAdminOrEngineer

# Create your views here.

#monthly jobs view

@api_view(['GET'])
def monthly_jobs(request):

    month = request.query_params.get('month')
    year = request.query_params.get('year')

    jobs = MaintainenceJobs.objects.all()
    
    if month and year:
        jobs = jobs.filter(
            scheduled_date__month=month,
            scheduled_date__year=year
        )

    serializer = CalendarJobSerializer(jobs,many=True)
    return Response(serializer.data)


#jobs by date

@api_view(['GET'])
def jobs_by_date(request):
    
    date = request.query_params.get('date')

    if not date:
        return Response({'ERROR':"DATE PARAMETER REQUIRED!!"},status=status.HTTP_400_BAD_REQUEST)
    
    jobs = MaintainenceJobs.objects.filter(scheduled_date=date)
    
    serializer = CalendarJobSerializer(jobs,many=True)
    return Response(serializer.data)