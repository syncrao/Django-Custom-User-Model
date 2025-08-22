from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # check if username is email
            user = UserModel.objects.filter(email=username).first()
            if not user:
                # if not email, check phone
                user = UserModel.objects.filter(phone=username).first()
            if user and user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
