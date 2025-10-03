from rest_framework import mixins, viewsets


class CreateMixin(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Миксин для создания объекта."""
    pass


class CreateRetrieveListMixin(
    CreateMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin
):
    """Миксин для создания. получения объекта и получение его списка."""
    pass


class CreateRetrieveListUpdateMixin(
    CreateRetrieveListMixin,
    mixins.UpdateModelMixin
):
    """
    Миксин для создания. получения,
    обновления объекта и получение его списка.
     """
    pass
