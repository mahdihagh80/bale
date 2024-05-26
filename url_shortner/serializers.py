from rest_framework import serializers
from django.conf import settings


class UrlSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=1000, required=True)

class ShortUrlSerializer(serializers.Serializer):
    short_url = serializers.CharField(max_length=settings.SHORT_URL_LENGTH)