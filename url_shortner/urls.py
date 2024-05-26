from django.urls import path
from .views import ShortenUrlView, RedirectUrlView
urlpatterns = [
    path('short/', ShortenUrlView.as_view()),
    path('redirect/<str:short_url>/', RedirectUrlView.as_view()),
]
