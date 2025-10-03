from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse, OpenApiExample

NOT_AUTH_USER = OpenApiResponse(
    response=OpenApiTypes.OBJECT,
    description='Не аутентифицированный пользователь',
    examples=[
        OpenApiExample(
            'Анонимный пользователь',
            value={'detail': 'Учетные данные не были предоставлены.'}
        ),
    ]
)


class UserDocs:
    me = extend_schema(
        summary='Возвращает информацию о пользователе',
        description='Возвращает данные текущего пользователя.',
        tags=['Пользователь'],
        responses={
            401: NOT_AUTH_USER
        }
    )
    patch_me = extend_schema(
        summary='Обновляет данные пользователя',
        description='Обновляет данные текущего пользователя.',
        tags=['Пользователь'],
        responses={
            401: NOT_AUTH_USER
        }
    )
    create = extend_schema(
        summary='Создать новое пользователя',
        description='Создает новое Пользователя с указанными параметрами.',
        tags=['Пользователь'],
        responses={
            400: OpenApiResponse(
                response=OpenApiTypes.OBJECT,
                description='Ошибки валидации',
                examples=[
                    OpenApiExample(
                        'Невалидные данные',
                        value={'example': 'Обязательное поле.'}
                    ),
                ]
            ),
        }
    )


users_viewset_docs = extend_schema_view(
    create=UserDocs.create
)
