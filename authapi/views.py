from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from django.conf import settings
from django.contrib import auth
import jwt


class RegisterView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        """
        Create User
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        data = request.data
        username = data.get('username', '')
        password = data.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth_token = jwt.encode({
                'username': user.username
            }, key=settings.JWT_SECRET_KEY, algorithm="HS256")
            data = {
                "user": UserSerializer(user).data,
                "token": auth_token
            }
            return Response(data)
        return Response({"detail": "Invalid Credentials Provided."}, status=status.HTTP_401_UNAUTHORIZED)
