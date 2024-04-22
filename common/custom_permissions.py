from rest_framework import permissions


class EmailVerified(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_email_verified
