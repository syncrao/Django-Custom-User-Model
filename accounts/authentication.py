from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate
from rest_framework import serializers
from accounts.models import User


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # default

    def validate(self, attrs):
        identifier = attrs.get("email")  # this will be email or phone
        password = attrs.get("password")

        # Try login with email
        user = authenticate(email=identifier, password=password)

        if user is None:
            # Try login with phone
            try:
                user_obj = User.objects.get(phone=identifier)
                user = authenticate(email=user_obj.email, password=password)
            except User.DoesNotExist:
                pass

        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        refresh = self.get_token(user)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
