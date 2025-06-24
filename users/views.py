from django.shortcuts import render
from .models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

# Create your views here.
def get_tokens_for_user(user):
    if not user.is_active:
        raise AuthenticationFailed("User is not active")

        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()

            return Response({
                "message": "Usuário cadastrado com sucesso!",
                "user": RegisterSerializer(user).data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "Ocorreu um erro ao cadastrar usuário. Tente novamente."
        }, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email').lower().strip()
        password = request.data.get('password')

        if not email or password:
            return Response({
                "message": 'Email e senha são obrigatórios'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = authenticate(email=email, password=password)
            token = get_tokens_for_user(user)

            return Response({
                "message": "Login efetuado com sucesso.",
                "token-refresh": token.refresh,
                "token-access": token.access
            }, status=status.HTTP_200_OK)
        except:
            return Response({
                "message": "Erro ao fazer login. Tente novamente!"
            }, status=status.HTTP_400_BAD_REQUEST)