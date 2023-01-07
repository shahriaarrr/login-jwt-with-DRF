from django.urls import path, include
from .Api.api import RegisterApi, LoginApi

urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('api/login', LoginApi().as_view()),
]