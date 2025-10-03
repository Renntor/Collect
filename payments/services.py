from django.utils import timezone
from rest_framework.serializers import ValidationError

from collects.models import Collect


class PaymentsService:

    @staticmethod
    def checking_time_collection(obj: Collect) -> None:
        """
        Проверка даты окончания сбора.
        """
        if obj.date_end < timezone.now():
            raise ValidationError('Сбор уже завершён.')
