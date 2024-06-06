from django.shortcuts import render

# Create your views here.
# rest_framework
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import get_user_model

from . import serializers
from .send_email import (
                        send_confirmation_email,
                        send_code_email,
                        )


User = get_user_model()


class RegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                send_confirmation_email(user=user.email, code=user.activation_code)
            return Response('Send on your email', status=201)
        return Response('Bad request!!!', status=400)


class ActivationView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Successfully activated!'}, status=200)
        except User.DoesNotExist:
            return Response({'msg': 'Link expired!'}, status=400)


''' Log in/out '''

class LoginView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)


class LogoutView(GenericAPIView):
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Successfully logged out!', status=204)


''' Restore '''
class ForgotPasswordView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        from random import randint
        serializer = serializers.ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            email = serializer.data.get('email')
            user = User.objects.get(email=email)
            user.activation_code = randint(1000, 9999)
            user.save()
            send_code_email(user=user)
            return Response(
                'check email',
                status=200
            )
        except User.DoesNotExist:
            return Response(
                'User with this email doesn\'t exist',
                status=400
            )


class RestoreView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.RestorePasswordSerializer
