from rest_framework.permissions import BasePermission
# TO DO:
# Custom permission class created for role-based authorization.
# Intended behavior:
# - Only ADMIN / SUPERUSER can access protected endpoints
# - Normal users should receive 403 Forbidden



class IsSuperUser(BasePermission):
    def has_permission(self,request,view):

            # Runs before the view executes
            # Decides whether the request should proceed
            # Must return:
            # True → Allow request
            # False → Deny request (403)

        #user must be login
        if not request.user.is_authenticated:
            return False

        # Only Django superuser is ADMIN
        return request.user.is_superuser       