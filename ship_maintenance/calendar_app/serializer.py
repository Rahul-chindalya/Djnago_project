from rest_framework import serializers
from jobs.models import MaintainenceJobs

class CalendarJobSerializer(serializers.ModelSerializer):
    ship_name = serializers.CharField(source='ship.name',read_only = True )

    class Meta:
        model = MaintainenceJobs
        fields = ['id','ship','ship_name','job_type','prority','status','scheduled_date'] 