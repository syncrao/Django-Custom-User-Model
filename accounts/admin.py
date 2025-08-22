from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "phone", "is_staff", "is_verified"]

      # Fields shown when editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("phone", "is_verified")}),
    )

    # Fields shown when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("phone", "is_verified")}),
    )

