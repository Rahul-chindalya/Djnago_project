from rest_framework.permissions import BasePermission
# TODO:
# Custom permission class created for role-based authorization.
# Intended behavior:
# - Only ADMIN / SUPERUSER can access protected endpoints
# - Normal users should receive 403 Forbidden
#
# Current status:
# - Permission logic implemented
# - Not functioning correctly (needs debugging)
#
# Possible checks:
# - Verify Profile.role value
# - Confirm authentication (Token/JWT/Session)
# - Ensure permission_classes applied to views

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