from django.contrib.auth import login, logout, authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework.views import APIView
import json
from django.http import JsonResponse

from .models import User
from .serializers import UserSerializer

class LoginView(APIView):
    def post(request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Success'}, status=200)
        else:
            return Response({'message': 'Неверный логин или пароль'}, status=400)
        # return Response({'message': 'Invalid request method'}, status=400)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return Response({'message': 'Logout success'}, status=200)
    return Response({'message': 'Invalid request method'}, status=400)

class RegisterView(APIView):
    def post(request):
        print('OK')
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        password_more = data.get('password_more')

        is_exists = User.objects.filter(username=username).exists()
        if is_exists:
            return Response({'message': 'Такой пользователь уже существует'}, status=400)
        if not all([username, password, email]):
            return Response({'message': 'Все поля обязательны'}, status=400)

        user = User.objects.create_user(username, email, password)
        login(request, user)
        return Response({'message': 'Success'}, status=201)
    # return Response({'message': 'Invalid request method'}, status=400)

@extend_schema(tags=['User'], methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @extend_schema(
        description='Создание пользователя',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Пользователь создан',
                response=serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @extend_schema(
        description='Список всех существующих пользователей',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class(many=True)
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        description='Получение сведений о пользователе по ID',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description = 'Комната не найдена'
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description='Обновление пользователя',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description='Обновление части данных пользователя',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление пользователя',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Пользователь удален успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Пользователь не найден',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
