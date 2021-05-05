from backend.password_reset import ResetPasswordEmail
from .views import *
from django.urls import path

urlpatterns=[
    path('api/user/', UserDetail.as_view()),
    path('api/login/', LoginTokenView.as_view()),
    path('api/register/', RegisterView.as_view()),
    path('api/reset/password', ResetPasswordEmail.as_view())
]