import pytest
from rest_framework import status

from collects.models import Collect


@pytest.mark.django_db(transaction=True)
class Test01Collect:
    URL_CREATE_LIST = '/api/v1/collects/'
    URL_RETRIEVE_PATCH = '/api/v1/collects/{id}/'


    def test_list_collect(self, client, collect, collect_two):
        """Проверка на возможность получить список сборов"""
        response = client.get(self.URL_CREATE_LIST)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) != 0
        assert len(response.data['results']) == Collect.objects.count()

    def test_retrieve_collect(self, client, collect_id):
        """Проверка на возможность получить конкретный сбор"""
        response = client.get(
            self.URL_RETRIEVE_PATCH.format(id=collect_id)
        )
        assert response.status_code == status.HTTP_200_OK


    def test_create_collect_not_authenticated(self, client, collect_data):
        """Проверка на запрет создать сбор анонимному пользователю"""
        response = client.post(self.URL_CREATE_LIST, data=collect_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_create_collect_authenticated(self, user_client, collect_data):
        """Проверка на возможность создать сбор"""
        response = user_client.post(self.URL_CREATE_LIST, data=collect_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == collect_data['name']


    def test_create_collect_with_error(self, user_client, collect_data_with_error):
        """Проверка на возможность создать сбор с ошибками"""
        response = user_client.post(self.URL_CREATE_LIST, data=collect_data_with_error)
        assert response.status_code == status.HTTP_400_BAD_REQUEST


    def test_patch_collect_authenticated(self, user_client, collect_id, collect_update_data):
        """Проверка на возможность редактировать сбор"""
        response = user_client.patch(
            self.URL_RETRIEVE_PATCH.format(id=collect_id),
            data=collect_update_data
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == collect_update_data['name']
        assert response.data['description'] == collect_update_data['description']

    def test_patch_collect_not_authenticated(self, client, collect_id, collect_update_data):
        """Проверка на запрет редактировать сбор анонимному пользователю"""
        response = client.patch(
            self.URL_RETRIEVE_PATCH.format(id=collect_id),
            data=collect_update_data
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_patch_collect_another_client(self, another_user_client, collect_id, collect_update_data):
        """Проверка на запрет редактировать сбор чужому пользователю"""
        response = another_user_client.patch(
            self.URL_RETRIEVE_PATCH.format(id=collect_id),
            data=collect_update_data
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN