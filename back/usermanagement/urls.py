from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import CustomUserCreate,BlacklistTokenUpdateView
# import debug_toolbar
from rest_framework_simplejwt.views import (
     TokenObtainPairView,
     TokenRefreshView,
)
app_name = 'usermanagement'

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", CustomUserCreate.as_view(), name="create_user"),
    path("logout/blacklist/", BlacklistTokenUpdateView.as_view(), name="blacklist"),

] 
