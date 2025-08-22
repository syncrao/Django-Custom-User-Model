from django.contrib import admin
from django.urls import path
from accounts.views import RegisterView, ProfileView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/profile/', ProfileView.as_view(), name='profile'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/logout/", LogoutView.as_view(), name="logout"),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
