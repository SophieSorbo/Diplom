from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):    # get, like and comment
        if request.method in permissions.SAFE_METHODS or request.method == 'POST':
            return True
        return obj.user == request.user