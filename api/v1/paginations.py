from rest_framework.pagination import PageNumberPagination

from collects.constatns import CollectConstants
from payments.constatns import PaymentConstants


class BasePageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'


class PaymentPageNumberPagination(BasePageNumberPagination):
    page_size = PaymentConstants.Pagination.Payment.PAGE_SIZE
    max_page_size = PaymentConstants.Pagination.Payment.MAX_PAGE_SIZE


class CollectPageNumberPagination(BasePageNumberPagination):
    page_size = CollectConstants.Pagination.Collect.PAGE_SIZE
    max_page_size = CollectConstants.Pagination.Collect.MAX_PAGE_SIZE
