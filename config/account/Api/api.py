from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from .serializer import RegisterSerializer, UserSerializer, LoginSerializer
from .utils import get_tokens_for_user

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = User.objects.get(username=serializer.data['username'])
            return Response(
                {
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                    **get_tokens_for_user(user),
                },
                status=status.HTTP_200_OK
            )
