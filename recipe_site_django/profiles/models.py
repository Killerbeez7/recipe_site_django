from django.contrib.auth import get_user_model
from django.db import models
# from .signals import *


UserModel = get_user_model()


class Profile(models.Model):
    first_name = models.CharField(
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        max_length=20,
        blank=True,
    )
    age = models.IntegerField(
        blank=True,
        null=True,
    )
    profile_image = models.ImageField(
        upload_to='profiles',
        blank=True,
    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    is_complete = models.BooleanField(
        default=False,
    )



