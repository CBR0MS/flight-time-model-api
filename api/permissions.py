from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class AllReadOnlyExceptAdmin(BasePermission):

    def has_permission(self, request, view):
        return bool(
            (request.user.is_authenticated and request.user.is_superuser) or
            (request.method in SAFE_METHODS and(request.user or request.user.is_authenticated))
        )