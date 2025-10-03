from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from .constatns import CollectConstants


class Collect(models.Model):

    class ReasonChoices(models.TextChoices):
        PLATFORM = 'PLATFORM', 'Развитие'
        COMMUNITY = 'COMMUNITY', 'Мероприятие'
        CHARITY = 'CHARITY', 'Благотворительность'

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        help_text='Пользователь создавший сбор'
    )
    name = models.CharField(
        max_length=CollectConstants.Lengths.MAX_LENGTH_NAME,
        verbose_name='Название',
        help_text='Названия сбора',
        validators=[
            MinLengthValidator(CollectConstants.Lengths.MIN_LENGTH_NAME)
        ]
    )
    reason = models.CharField(
        max_length=CollectConstants.Lengths.MAX_LENGTH_REASON,
        choices=ReasonChoices.choices,
        verbose_name='Повод',
        help_text='Повод сбора пожертвований',
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Описание',
        help_text='Описание цели сбора пожертвований'
    )
    total_goal_amount = models.PositiveBigIntegerField(
        blank=True,
        null=True,
        verbose_name='Планируемый сбор',
        help_text='Планируемый сбор пожертвований',
        validators=[
            MinValueValidator(
                CollectConstants.Lengths.MIN_VALUE_TOTAL_GOAL_AMOUNT
            )
        ]
    )
    image = models.ImageField(
        blank=True,
        null=True,
        verbose_name='Обложка',
        help_text='Обложка сбора пожертвований'
    )
    date_end = models.DateTimeField(
        verbose_name='Время окончания',
        help_text='Время окончания сбора пожертвований'
    )
    target_amount = models.PositiveIntegerField(
        verbose_name='Цель пожертвований',
        help_text='Цель для количества пожертвований',
        validators=[
            MinValueValidator(
                CollectConstants.Lengths.MIN_VALUE_TARGET_AMOUNT
            )
        ]
    )

    def __str__(self):
        return (f'Сбор {self.name}. '
                f'Планируемая сумма сбора {self.total_goal_amount}.')
