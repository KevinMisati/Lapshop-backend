from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth import views as auth_views
from .views import register_user, custom_login_view, logout_view, password_reset_confirm,password_reset_request

urlpatterns = [
    path('token/',custom_login_view,name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/',register_user,name='register_user'),
    path('logout/',logout_view,name='logout'),
    path('password-reset/',password_reset_request,name='password_reset'),

    path('password-reset-confirm/<uidb64>/token/',password_reset_confirm,name='password_reset_confirm'),

    path('password-reset-done/',auth_views.PasswordChangeDoneView.as_view(),name='password_reset'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_done'),
]


