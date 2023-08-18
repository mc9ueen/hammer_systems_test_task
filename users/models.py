from django.contrib.auth.models import AbstractUser
from django.db import models

from utils.generate_code import generate_code


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=12,
                                    unique=True,
                                    null=False,
                                    blank=False,
                                    verbose_name='Номер телефона',)
    invite_code = models.CharField(max_length=6,
                                   null=False,
                                   blank=False,
                                   unique=True,
                                   default=generate_code())
    referral_code = models.CharField(max_length=6,
                                     null=True,
                                     blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['phone_number', ]

    class Meta:
        default_related_name = 'users'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.phone_number
