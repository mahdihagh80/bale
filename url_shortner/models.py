from django.db import models
from django.conf import settings

class Url(models.Model):
    original_url = models.CharField(max_length=1000)
    short_url = models.CharField(max_length=settings.SHORT_URL_LENGTH, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['original_url']),
        ]

