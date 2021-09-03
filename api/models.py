from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Diary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    weather = models.CharField(max_length=15)
    # photo = models.ImageField(null=True, blank=True)
    content = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    content_len = models.IntegerField(default=0)

    def __str__(self):
        return self.title
