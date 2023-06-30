from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=10, unique=True)
    password = models.CharField(_("password"), max_length=128)

    code = models.CharField(max_length=3)

    USERNAME_FIELD = 'username'
