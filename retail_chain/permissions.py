from rest_framework.permissions import BasePermission


class IsActivePermissions(BasePermission):
    """Проверка на статус активности пользователя"""

    def has_permission(self, request, view):
        return request.user.is_active
