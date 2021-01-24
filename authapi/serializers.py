from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=45, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255, min_length=5)
    first_name = serializers.CharField(max_length=255, min_length=2)
    last_name = serializers.CharField(max_length=255, min_length=2)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email__exact=email).exists():
            raise serializers.ValidationError({'email': ('Account already registered using this email-id.')})
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=256, write_only=True, min_length=8)
    username = serializers.CharField(max_length=256, min_length=1)

    class Meta:
        model = User
        fields = ['username', 'password']
