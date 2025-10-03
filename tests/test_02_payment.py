import pytest
from rest_framework import status

from payments.models import Payment


@pytest.mark.django_db(transaction=True)
class Test02Payment:
    URL_CREATE_LIST = '/api/v1/payments/'
    URL_RETRIEVE = '/api/v1/payments/{id}/'


    def test_list_payment(self, client, payment, payment_two):
        """Проверка на возможность получить список пожертвований"""
        response = client.get(self.URL_CREATE_LIST)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) != 0
        assert len(response.data['results']) == Payment.objects.count()

    def test_retrieve_payment(self, client, payment_anonymous_id):
        """Проверка на возможность получить конкретный пожертвование"""
        response = client.get(
            self.URL_RETRIEVE.format(id=payment_anonymous_id)
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data['amount'] == None


    def test_create_payment_not_authenticated(self, client, payment_data):
        """Проверка на запрет создать пожертвование"""
        response = client.post(self.URL_CREATE_LIST, data=payment_data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


    def test_create_payment_authenticated(self, user_client, payment_create_data):
        """Проверка на возможность создать пожертвование"""
        response = user_client.post(self.URL_CREATE_LIST, data=payment_create_data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['amount'] == payment_create_data['amount']

