from django.shortcuts import render

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response

from ships.models import Ship
from components.models import Component
from jobs.models import MaintainenceJobs
from django.utils import timezone
from accounts.permissions import IsSuperUser

# Create your views here.
@api_view(['GET'])
@permission_classes([IsSuperUser])
def dashboard_summery(request):
    total_ship = Ship.objects.count()

    total_components = Component.objects.count()
    over_due_components = Component.objects.filter(last_maintenance=timezone.now().date()).count()

    pending_jobs = MaintainenceJobs.objects.filter(status='PENDING').count()
    in_progress_jobs =MaintainenceJobs.objects.filter(status='IN_PROGRESS').count()
    completed_jobs = MaintainenceJobs.objects.filter(status='COMPLETED').count()

    data = {
        "total_ships": total_ship,
        "total_components":total_components,
        "over_due_components":over_due_components,
        "pending_jobs":pending_jobs,
        "in_progress_jobs":in_progress_jobs,
        "completed_jobs":completed_jobs
    }
    return Response(data)