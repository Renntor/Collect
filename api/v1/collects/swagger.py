from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiExample

from api.v1.users.swagger import NOT_AUTH_USER


class CollectDocs:
    list = extend_schema(
        summary='Получить список сборов',
        description='Возвращает список всех доступных сборов с пагинацией.',
        tags=['Сбор'],
    )
    retrieve = extend_schema(
        summary='Получить информацию о сборе',
        description='Возвращает данные конкретного сбора по его ID.',
        tags=['Сбор'],
    )
    create = extend_schema(
        summary='Создать новый сбор',
        description='Создает новый сбор с указанными параметрами.',
        tags=['Сбор'],
        responses={
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Ошибки валидации',
                examples=[
                    OpenApiExample(
                        'Невалидные данные',
                        value={'example': 'Обязательное поле.'}
                    ),
                    OpenApiExample(
                        'Не правильная дата окончания сбора',
                        value={'example': 'Дата окончания сбора не может быть меньше текущей даты'}
                    ),
                ]
            ),
            401: NOT_AUTH_USER
        }
    )
    partial_update = extend_schema(
        summary='Изменить данные сбора',
        description='Позволяет обновить часть данных о сборе.',
        tags=['Сбор'],
        responses={
            401: NOT_AUTH_USER,
            403: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Отказано в доступе',
                examples=[
                    OpenApiExample(
                        'Изменение чужого сбора',
                        value={'detail': 'У вас недостаточно прав для выполнения данного действия'}
                    )
                ]
            )
        }
    )


collect_viewset_docs = extend_schema_view(
    list=CollectDocs.list,
    retrieve=CollectDocs.retrieve,
    create=CollectDocs.create,
    partial_update=CollectDocs.partial_update,
)
