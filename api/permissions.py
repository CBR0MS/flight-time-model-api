from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class AllReadOnlyExceptAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (request.method in SAFE_METHODS and
            (request.user or
            request.user.is_authenticated)) or 
            (request.user.is_authenticated and request.user.is_admin)
        )