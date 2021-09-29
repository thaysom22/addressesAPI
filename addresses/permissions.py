from rest_framework.permissions import BasePermission


class CurrentUserIsOwnerOrAdmin(BasePermission):
	
    def has_object_permission(self, request, view, instance):
        return bool(instance.user == request.user or request.user.is_staff)