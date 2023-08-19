from rest_framework.permissions import BasePermission

class IsDepartmentAdmin(BasePermission):
    """
    Custom permission to only allow department administrators to access the object.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the request user is a department administrator.
        # Here, we assume that the user model has an attribute 'is_department_admin' to check.
        return request.user.is_department_admin
