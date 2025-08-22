from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "phone", "password")

    def validate(self, data):
        # Require at least email or phone
        print(f"username: {data}")

        if not data.get("email") and not data.get("phone"):
            raise serializers.ValidationError("You must provide either email or phone.")
        
        

        if not data.get("password"):
            raise serializers.ValidationError("Password is required.")
        
        if not data.get("username"):
            raise serializers.ValidationError("Username is required.")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.get("username"),
            email=validated_data.get("email"),
            phone=validated_data.get("phone"),
            password=validated_data.get("password"),
        )
        return user

