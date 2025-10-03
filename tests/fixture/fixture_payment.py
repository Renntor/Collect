import pytest
from payments.models import Payment


@pytest.fixture
def payment_data(user, collect):
    return {
        'user': user,
        'collect': collect,
        'amount': 1000
    }

@pytest.fixture
def payment_create_data(user, collect_id):
    return {
        'user': user,
        'collect': collect_id,
        'amount': 1000
    }

@pytest.fixture
def payment_data_two(another_user, collect):
    return {
        'user': another_user,
        'collect': collect,
        'amount': 5000
    }

@pytest.fixture
def payment_data_anonymous(another_user, collect):
    return {
        'user': another_user,
        'collect': collect,
        'amount': 5000,
        'is_anonymous': True
    }


@pytest.fixture
def payment(payment_data):
    return Payment.objects.create(**payment_data)

@pytest.fixture
def payment_two(payment_data_two):
    return Payment.objects.create(**payment_data_two)

@pytest.fixture
def payment_anonymous(payment_data_anonymous):
    return Payment.objects.create(**payment_data_anonymous)

@pytest.fixture
def payment_id(payment):
    return payment.id

@pytest.fixture
def payment_two_id(payment_two):
    return payment_two.id

@pytest.fixture
def payment_anonymous_id(payment_anonymous):
    return payment_anonymous.id
