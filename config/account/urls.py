from django.urls import path, include
from .Api.api import RegisterApi

urlpatterns = [
      path('api/register', RegisterApi.as_view()),
]