from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponseRedirect

from .shorten_algorithms import hash_base64_shorten
from .serializers import UrlSerializer, ShortUrlSerializer
from .models import Url


class ShortenUrlView(APIView):

    def post(self, request):
        serializer = UrlSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        original_url = serializer.validated_data['url']
        short_url = hash_base64_shorten(original_url)

        if 'http' not in original_url:
            original_url = 'http://' + original_url

        try:
            obj, _ = Url.objects.get_or_create(original_url=original_url, short_url=short_url)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response(ShortUrlSerializer({'short_url': short_url}).data, status=status.HTTP_201_CREATED)


class RedirectUrlView(APIView):
    def get(self, request, *args, **kwargs):
        short_url = kwargs.get('short_url', None)

        try:
            obj = Url.objects.get(short_url=short_url)
        except Url.DoesNotExist:
            return Response({'error': 'invalid short url'}, status=status.HTTP_404_NOT_FOUND)

        url = obj.original_url
        return HttpResponseRedirect(url)



