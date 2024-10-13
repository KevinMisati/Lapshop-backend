from django.shortcuts import render
from django.contrib.auth import authenticate

# Create your views here.

from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.models import Token
from .serializers import LoginSerializer

@api_view(['POST'])
def register_user(request):
    try:
        username = request.data['username']
        password = request.data['password']
        email = request.data.get('email','')

        validate_password(password)

        user = User.objects.create_user(username=username,password=password,email=email)
        user.save()

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh':str(refresh),
            'access':str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    except KeyError:
        return Response({'error':'Please provide username and password'})
    except ValidationError as e:
        return Response({'error':str(e)},status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_view(request):
    try:
        refresh_token = request.data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response(status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def custom_login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({'detail': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request=request, email=email, password=password)

    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_id': user.id,
            'email': user.email,
        }, status=status.HTTP_200_OK)
    else:
        return Response({'detail': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
