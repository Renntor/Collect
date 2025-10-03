import pytest
from django.core.cache import cache
from django.conf import settings

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken



@pytest.fixture(autouse=True, scope="session")
def set_email_backend():
    settings.EMAIL_BACKEND = 'django.core.mail.backends.locmen.EmailBackend'


@pytest.fixture(autouse=True)
def clear_cache():
    """Очищает кеш перед и после каждого теста"""
    cache.clear()
    yield
    cache.clear()

@pytest.fixture
def user_data():
    return {
        'first_name': 'Тест',
        'last_name': 'Первый',
        'patronymic': 'Первейший',
        'email': 'test1@mail.ru',
        'password': '1234'
    }
@pytest.fixture
def another_user_data():
    return {
        'first_name': 'Тест',
        'last_name': 'Второй',
        'email': 'test2@mail.ru',
        'password': '1234'
    }

@pytest.fixture
def user_edit_data():
    return {
        'first_name': 'Тестер',
        'last_name': 'Второй'
    }


@pytest.fixture
def user(django_user_model, user_data):
    user = django_user_model(**user_data)
    user.set_password(user_data['password'])
    user.save()
    return user


@pytest.fixture
def another_user(django_user_model, another_user_data):
    another_user = django_user_model(**another_user_data)
    another_user.set_password(another_user_data['password'])
    another_user.save()
    return another_user


@pytest.fixture
def user_client(user):
    client = APIClient()
    token = AccessToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client


@pytest.fixture
def another_user_client(another_user):
    client = APIClient()
    token = AccessToken.for_user(another_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
    return client
