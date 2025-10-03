from celery import shared_task
from django.core.mail import send_mail

from config import settings as settings_django


@shared_task
def send_notification_collect(email: str, collect_name: str):
    """
    Отправка письма об успешном создании сбора.
    """
    to = [email]
    send_mail(
        subject='Создан новый сбор',
        message=f'Ваш новый сбор - {collect_name} был успешно создан.',
        from_email=settings_django.EMAIL_HOST_USER,
        recipient_list=to,
    )
