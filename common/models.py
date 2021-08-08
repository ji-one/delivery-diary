from django.db import models

# Create your models here.
from django.contrib.auth.models import UserManager, AbstractUser, BaseUserManager


class User(AbstractUser):
    nickname = models.CharField(blank=False, max_length=16)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='images/')
    birthday = models.DateField(blank=True, null=True)
    phone_number = models.CharField(blank=False, max_length=16)
    address = models.CharField(blank=False, max_length=128)
    objects = UserManager()
