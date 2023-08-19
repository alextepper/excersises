from rest_framework.permissions import BasePermission

class IsDepartmentAdmin(BasePermission):
    def has_permission(self, request, view):
        # Check if the user is a member of the 'department_admin' group
        return request.user.groups.filter(name="Department Admin").exists()

