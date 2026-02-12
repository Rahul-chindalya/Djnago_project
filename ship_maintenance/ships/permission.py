from rest_framework.permissions import BasePermission
from accounts.models import Profile

class ISAdminOrEngineer(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        
        profile = Profile.objects.filter(user=request.user).first()

        if not profile:
            return False
        
        return profile.role in ['ADMIN','ENGINEER']