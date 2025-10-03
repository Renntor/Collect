from rest_framework.permissions import AllowAny, IsAuthenticated

from api.v1.mixins import CreateRetrieveListMixin
from api.v1.paginations import PaymentPageNumberPagination
from api.v1.payments.serializers import PaymentSerializers
from api.v1.payments.swagger import payments_viewset_docs
from payments.constatns import PaymentConstants
from payments.models import Payment
from payments.services import PaymentsService
from payments.tasks import send_notification_payment
from utils.utils import BaseService


@payments_viewset_docs
class PaymentViewSet(CreateRetrieveListMixin):
    queryset = Payment.objects.all().order_by('id')
    serializer_class = PaymentSerializers
    pagination_class = PaymentPageNumberPagination

    def get_permissions(self):
        match self.action:
            case 'create':
                return (IsAuthenticated(),)
            case 'list' | 'retrieve':
                return (AllowAny(),)

    def perform_create(self, serializer):
        PaymentsService.checking_time_collection(
            serializer.validated_data['collect']
        )
        serializer.save(user=self.request.user)
        send_notification_payment.delay(
            self.request.user.email,
        )

    def _generate_cache_key_collect_list(self, request, *args, **kwargs):
        """Генерация ключа кеша для списка пожертвований."""
        page_param = request.query_params.get('page', '1')
        page_size = request.query_params.get('page_size', '')

        cached_key = PaymentConstants.Cache.Payment.KEY.format(
            search=BaseService.generate_cache_key(
                f'{page_param}:{page_size}'
            )
        )
        return cached_key

    @BaseService.cache_response_decorator(
        _generate_cache_key_collect_list,
        PaymentConstants.Cache.Payment.LIFETIME
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
