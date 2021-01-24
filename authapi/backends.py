import jwt
from django.contrib.auth.models import User
from rest_framework import authentication
from django.conf import settings
from rest_framework import exceptions


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        authData = authentication.get_authorization_header(request=request)
        if not authData:
            return None
        prefix, token = authData.decode('utf-8').split(' ')
        try:
            payload = jwt.decode(token, key=settings.JWT_SECRET_KEY, algorithms="HS256")
            user = User.objects.get(username=payload['username'])
            return (user, token)
        except jwt.DecodeError as e:
            print(e)
            raise exceptions.AuthenticationFailed('Invalid Token Provided.')
        except jwt.ExpiredSignatureError as e:
            raise exceptions.AuthenticationFailed('Expired Token Provided.')
