from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register_user, custom_login_view

urlpatterns = [
    path('token/',custom_login_view,name='token_obtain_pair'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('register/',register_user,name='register_user'),
    path('logout/',register_user,name='logout')
]


