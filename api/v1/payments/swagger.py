from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiExample

from api.v1.users.swagger import NOT_AUTH_USER


class PaymentDocs:
    list = extend_schema(
        summary='Получить список пожертвований',
        description='Возвращает список всех доступных пожертвований с пагинацией.',
        tags=['Пожертвования'],
    )
    retrieve = extend_schema(
        summary='Получить информацию о пожертвовании',
        description='Возвращает данные конкретного пожертвовании по его ID.',
        tags=['Пожертвования'],
    )
    create = extend_schema(
        summary='Создать новое пожертвование',
        description='Создает новое Пожертвования с указанными параметрами.',
        tags=['Пожертвования'],
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
                        'Превышение даты сбора',
                        value={'example': 'Сбор уже завершён.'}
                    ),
                ]
            ),
            401: NOT_AUTH_USER
        }
    )


payments_viewset_docs = extend_schema_view(
    list=PaymentDocs.list,
    retrieve=PaymentDocs.retrieve,
    create=PaymentDocs.create
)
