from django.contrib.auth import login, logout, authenticate
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
import json

from .models import User
from .serializers import UserSerializer

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # создание токена (если используете JWT)
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': 'Success',
                'user_id': user.id,
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'username': user.username,
                # другие данные пользователя
            }, status=200)
        else:
            return Response({'message': 'Неверный логин или пароль'}, status=400)
    return Response({'message': 'Invalid request method'}, status=400)

@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            refresh_token = data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout success'}, status=200)
        except Exception as e:
            return Response({'message': 'Invalid refresh token'}, status=400)
    return Response({'message': 'Invalid request method'}, status=400)

@api_view(['POST'])
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        password_confirm = data.get('password_more')
        email = data.get('email')

        is_exists = User.objects.filter(username=username).exists()
        if is_exists:
            return Response({'message': 'Такой пользователь уже существует'}, status=status.HTTP_400_BAD_REQUEST)
        if not all([username, password, email]):
            return Response({'message': 'Все поля обязательны'}, status=status.HTTP_400_BAD_REQUEST)
        if password != password_confirm:
            return Response({'message':'Пароли не совпадают'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username, email, password)
        login(request, user)
        return Response({'message': 'Success'}, status=201)
    return Response({'message': 'Invalid request method'}, status=400)

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
