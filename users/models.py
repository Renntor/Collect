from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from .constants import UserConstants


class User(AbstractUser):
    """
    Кастомная модель пользователя.
    Вместо username уникальный идентификатор используется email.
    """
    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Почта',
        help_text='Электронная почта пользователя'
    )
    first_name = models.CharField(
        max_length=UserConstants.Lengths.MAX_LENGTH_FIRST_NAME,
        verbose_name='Имя',
        help_text='Имя пользователя',
        validators=[
            MinLengthValidator(UserConstants.Lengths.MIN_LENGTH_FIRST_NAME)
        ]
    )
    last_name = models.CharField(
        max_length=UserConstants.Lengths.MAX_LENGTH_LAST_NAME,
        verbose_name='Фамилия',
        help_text='Фамилия пользователя',
        validators=[
            MinLengthValidator(UserConstants.Lengths.MIN_LENGTH_LAST_NAME)
        ]
    )
    patronymic = models.CharField(
        max_length=UserConstants.Lengths.MAX_LENGTH_PATRONYMIC,
        verbose_name='Отчество',
        help_text='Отчество пользователя',
        blank=True,
        null=False,
        validators=[
            MinLengthValidator(UserConstants.Lengths.MIN_LENGTH_PATRONYMIC)
        ]
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        return f'{self.first_name} {self.last_name} {self.patronymic}'.strip()
