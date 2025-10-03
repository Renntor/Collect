import pytest
from rest_framework import status
from users.models import User


@pytest.mark.django_db(transaction=True)
class Test00User:
    URL_CREATE = '/api/v1/users/'
    URL_ME = '/api/v1/users/me/'

    def test_create_user(
            self,
            client,
            user_data
    ):
        """Проверка на создание пользователя"""
        response = client.post(self.URL_CREATE, data=user_data)
        assert response.status_code == status.HTTP_201_CREATED
        user = User.objects.first()
        assert user.email == user_data['email']


    def test_me_not_authenticated(self, client):
        """Проверка на доступ не авторизированного пользователя"""
        response = client.get(self.URL_ME)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_me_authenticated(self, user_client):
        """Проверка на доступ авторизированного пользователя"""
        response = user_client.get(self.URL_ME)
        assert response.status_code == status.HTTP_200_OK


    def test_patch_me_not_authenticated(self, client, user_edit_data):
        """Проверка на возможность не авторизированного пользователя менять свои данные"""
        response = client.patch(self.URL_ME, data=user_edit_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_patch_me__authenticated(self, user_client, user_edit_data):
        """Проверка на возможность авторизированного пользователя менять свои данные"""
        response = user_client.patch(self.URL_ME, data=user_edit_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['first_name'] == user_edit_data['first_name']
