from rest_framework.permissions import IsAuthenticated


class IsOwnerCollect(IsAuthenticated):
    """
    Кастомная проверка владельца сбора.
    """

    def has_object_permission(self, request, view, obj):
        owner = obj.user

        if owner == request.user:
            return True
