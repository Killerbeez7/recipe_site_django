from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from recipe_site_django.recipe_site_auth.managers import RecipeSiteUserManager


class RecipeSiteUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    object = RecipeSiteUserManager()


# class Profile(models.Model):
#     profile_image = models.ImageField(
#         upload_to='profiles',
#     )
#     user = models.OneToOneField(
#         RecipeSiteUser,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )
