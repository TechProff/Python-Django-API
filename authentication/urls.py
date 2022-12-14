from django.urls import path
from .views import PasswordTokenCheckAPI, RegisterView, RequestPasswordResetEmail, SetNewPasswordAPIView, VerifyEmail, LoginAPIView
from rest_framework_simplejwt.views import (
   TokenRefreshView,
)
urlpatterns = [
   path('register', RegisterView.as_view(), name='register'),
   path('email-verify', VerifyEmail.as_view(), name='verify-email'),
   path('login', LoginAPIView.as_view(), name='login'),
   path('token/refresh', TokenRefreshView.as_view(), name='token'),
   path('request-reset-email', RequestPasswordResetEmail.as_view(), name='request-reset-email'),
   path('password-reset/<uidb64>/<token>', PasswordTokenCheckAPI.as_view(), name='password-reset-confirm'),
   path("password-reset-complete", SetNewPasswordAPIView.as_view(), name="password-reset-complete")
]