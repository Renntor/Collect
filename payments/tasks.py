from celery import shared_task
from django.core.mail import send_mail

from config import settings as settings_django


@shared_task
def send_notification_payment(email: str):
    """
    Отправка письма об успешном пожертвовании
    """
    to = [email]
    send_mail(
        subject='Пожертвование',
        message=f'Ваше пожертвование был успешно отправлено.',
        from_email=settings_django.EMAIL_HOST_USER,
        recipient_list=to,
    )
