from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.v1.collects.serializers import (CollectsSerializers,
                                         PatchCollectsSerializers)
from api.v1.collects.swagger import collect_viewset_docs
from api.v1.mixins import CreateRetrieveListUpdateMixin
from api.v1.paginations import CollectPageNumberPagination
from api.v1.permissions import IsOwnerCollect
from collects.constatns import CollectConstants
from collects.models import Collect
from collects.tasks import send_notification_collect
from utils.utils import BaseService


@collect_viewset_docs
class CollectViewSet(CreateRetrieveListUpdateMixin):
    queryset = Collect.objects.all().order_by('id')
    pagination_class = CollectPageNumberPagination
    http_method_names = ['get', 'patch', 'post']
    parser_classes = (MultiPartParser, FormParser)

    def get_permissions(self):
        match self.action:
            case 'create':
                return (IsAuthenticated(),)
            case 'partial_update':
                return (IsOwnerCollect(),)
            case _:
                return (AllowAny(),)

    def get_serializer_class(self):
        match self.action:
            case 'partial_update':
                return PatchCollectsSerializers
            case _:
                return CollectsSerializers

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        send_notification_collect.delay(
            self.request.user.email,
            serializer.validated_data['name']
        )

    def _generate_cache_key_collect_list(self, request, *args, **kwargs):
        """Генерация ключа кеша для списка сборов."""
        page_param = request.query_params.get('page', '1')
        page_size = request.query_params.get('page_size', '')

        cached_key = CollectConstants.Cache.Collect.KEY.format(
            search=BaseService.generate_cache_key(
                f'{page_param}:{page_size}'
            )
        )
        return cached_key

    @BaseService.cache_response_decorator(
        _generate_cache_key_collect_list,
        CollectConstants.Cache.Collect.LIFETIME
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
