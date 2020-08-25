from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    message = 'Permission denied.'

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        elif request.user.id == obj.user.id:
            return True
        return False
