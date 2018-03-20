from accounts import validator
from accounts import serializers
from accounts import services
from accounts import permissions as accounts_permissions
from accounts import models as accounts_models
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.settings import api_settings
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from storebook import settings
from django.contrib.auth.hashers import make_password

class LoginView(APIView):
    permission_classes = [permissions.AllowAny,]

    def post(self, request):
        data = request.data
        if not data.get('username'):
            return Response({'detail': 'the username field cant be empty'}, status=status.HTTP_400_BAD_REQUEST)
        if not data.get('password'):
            return Response({'detail': 'the password field cant be empty'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = accounts_models.User.objects.get(
                Q(username__iexact=data.get('username')) | Q(email__iexact=data.get('username')))
        except accounts_models.User.DoesNotExist:
            return Response({'detail': 'The username does not exits, please register a new account'},
                            status=status.HTTP_404_NOT_FOUND)
        if not user.is_active:
            return Response({'detail': 'Inactive user, confirm your account to gain access to the system'},
                            status=status.HTTP_401_UNAUTHORIZED)
        if not user.check_password(data.get('password')):
            return Response({'detail': 'Invalid password, please enter the correct password'},
                            status=status.HTTP_400_BAD_REQUEST)
        #creation of token with django-jwt
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return Response({'token': token, 'username': user.username, 'id': user.id})


class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated, accounts_permissions.IsOwnerOrReadOnly]

    def get(self, request):
        return Response({'deatil':'entro'})

class LoginFacebookView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        return Response({})


class LoginInstagramView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        return Response({})


class LoginGoogleView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        return Response({})


class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        return Response({})

from django.contrib.auth.models import Group
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def assign_group(self, user):
        group = Group.objects.get(name='Normal')
        if not group:
            print("no exitse el grupo")
        else:
            user.groups.add(group)
        #user.save()
        
    def post(self, request):
        data = request.data
        user = accounts_models.User.objects.create(
            username=data.get('username'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            email=data.get('email'),
            password=make_password(data.get('password'))
        )
        print(user)
        self.assign_group(user)
        return Response({"detail":"usario creado"}, status=status.HTTP_201_CREATED)

class CountryView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request):
        print(request.user)
        country = accounts_models.Country.objects.create(
            name=request.data.get('name')
        )
        return Response({"detail": "creado"}, status=status.HTTP_201_CREATED)

class RequestRecoverPasswordView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        return Response({})


class RecoverPasswordView(APIView):
    permission_classes = [permissions.AllowAny, ]

    def post(self, request):
        return Response({})


