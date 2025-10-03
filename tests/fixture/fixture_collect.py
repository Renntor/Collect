from django.utils import timezone
from datetime import timedelta

import pytest
from collects.models import Collect


@pytest.fixture
def collect_data(user):
    return {
        'user': user,
        'name': 'Первое пожертвование',
        'reason': Collect.ReasonChoices.CHARITY,
        'date_end': timezone.now() + timedelta(days=1),
        'target_amount': 5000
    }

@pytest.fixture
def collect_update_data(user):
    return {
        'name': 'Тестовое',
        'target_amount': 10000,
        'description': 'new'
    }

@pytest.fixture
def collect_data_two(another_user):
    return {
        'user': another_user,
        'name': 'Второе пожертвование',
        'reason': Collect.ReasonChoices.PLATFORM,
        'date_end': timezone.now() + timedelta(days=2),
        'target_amount': 1000
    }

@pytest.fixture
def collect_data_with_error(another_user):
    return {
        'user': another_user,
        'name': 'Второе пожертвование',
        'reason': Collect.ReasonChoices.PLATFORM,
        'date_end': timezone.now() - timedelta(days=2),
        'target_amount': 1000
    }


@pytest.fixture
def collect(collect_data):
    return Collect.objects.create(**collect_data)


@pytest.fixture
def collect_two(collect_data_two):
    return Collect.objects.create(**collect_data_two)


@pytest.fixture
def collect_id(collect):
    return collect.id

@pytest.fixture
def collect_two_id(collect_two):
    return collect_two.id

