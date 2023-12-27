from .views import *
from rest_framework_simplejwt.views import TokenBlacklistView
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('verify/', VerifyAccount.as_view()),

    path('login/', TokenObtainPairView.as_view()),
    path('new_password/', ChangePasswordView.as_view()),
    path('new_username/', ChangeUsernameView.as_view()),
    path('forgot_password/', ForgotPasswordView.as_view()),
    path('reset_password/', ResetPasswordView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())

]