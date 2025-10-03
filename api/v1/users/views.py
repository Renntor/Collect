from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.v1.mixins import CreateMixin
from api.v1.users.serializers import PatchUserSerializer, UserSerializer
from api.v1.users.swagger import users_viewset_docs, UserDocs
from users.models import User


@users_viewset_docs
class UserViewSet(CreateMixin):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return UserSerializer
            case _:
                return PatchUserSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @UserDocs.me
    @action(detail=False, methods=['get'], url_path='me',
            permission_classes=[IsAuthenticated])
    def me(self, request):
        serializer = self.get_serializer(self.request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @UserDocs.patch_me
    @me.mapping.patch
    def patch_me(self, request):
        serializer = self.get_serializer(
            request.user, data=request.data, partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
