from django.urls import path
from .import views

urlpatterns = [
    path('calander/monthly-jobs/',views.monthly_jobs),
    path('calander/jobs-by-date/',views.jobs_by_date),
]