from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField('Никнейм', max_length=255)
    image = models.ImageField(upload_to='media/users/', blank=True, null=True)
