from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.collects.views import CollectViewSet
from api.v1.payments.views import PaymentViewSet
from api.v1.users.views import UserViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register(
    'users',
    UserViewSet,
    basename='users'
)

v1_router.register(
    'payments',
    PaymentViewSet,
    basename='payments'
)

v1_router.register(
    'collects',
    CollectViewSet,
    basename='collects'
)

urlpatterns = [
    path('', include(v1_router.urls)),
    path('auth/', include('djoser.urls.jwt')),

]
