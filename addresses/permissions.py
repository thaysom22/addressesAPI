from rest_framework.permissions import BasePermission


class CurrentUserIsOwner(BasePermission):
	
	def has_object_permission(self, request, view, instance):
		return instance.user == request.user