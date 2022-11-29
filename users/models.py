from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    birthday = models.DateTimeField(
        'день рождения',
        blank=True,
        null=True,
    )
