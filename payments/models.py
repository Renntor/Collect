from django.core.validators import MinValueValidator
from django.db import models

from .constatns import PaymentConstants


class Payment(models.Model):

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь отправивший пожертвование'
    )
    collect = models.ForeignKey(
        'collects.Collect',
        on_delete=models.CASCADE,
        verbose_name='Сбор',
        help_text='Сбор, к которому относится пожертвование',
        related_name='donor'
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время',
        help_text='Дата и время отправки пожертвования'
    )
    amount = models.PositiveIntegerField(
        verbose_name='Сумма',
        help_text='Сумма пожертвования',
        validators=[
            MinValueValidator(PaymentConstants.Lengths.MIN_VALUE_AMOUNT)
        ]
    )
    is_anonymous = models.BooleanField(
        default=False,
        verbose_name='Скрытая',
        help_text='Скрытая сумма пожертвования'
    )

    def __str__(self):
        if self.is_anonymous:
            return f'{self.user.get_full_name()} отправил пожертвование.'
        else:
            return f'{self.user.get_full_name()} отправил - {self.amount}'
