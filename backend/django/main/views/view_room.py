from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework.decorators import action
import json

from usermanager.models import User
from ..serializers import RoomSerializer
from ..models import Room
from ..controllers.controller_room import *

@extend_schema(tags=['Room'])
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @extend_schema(
        description='Создание комнаты',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Комната создана',
                response=serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def create(self, request, *args, **kwargs):
        user = request.user
        try:
            response = create_room(user)
            data = self.get_serializer(response).data
            return Response(data, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Обновление комнаты',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Successful response',
                response=serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def update(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')

        data = json.loads(request.body)
        status = data.get('status')
        name = data.get('name')
        init_score = data.get('init_score')
        is_private = data.get('is_private')
        player_count = data.get('player_count')
        try:
            room = Room.objects.get(id=room_id)
            response, code = update_room(room, status, name, init_score, is_private, player_count)
            return Response(response, status=code)
        except Room.DoesNotExist:
            return Response({'error': 'Комната не найдена'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Список всех существующих комнат',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class(many=True)
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)

    @action(methods=['get'], detail=True)
    def join(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')
        user = request.user

        try:
            room = Room.objects.get(id=room_id)
            response, code = join_to_room(room, user)
            return Response(response, code)
        except (Room.DoesNotExist, User.DoesNotExist):
            return Response({'error': 'Комната или пользователь не найдены'}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def leave(self, request, *args, **kwargs):
        room_id = kwargs.get('pk')
        user = request.user

        try:
            room = Room.objects.get(id=room_id)
            player = Player.objects.get(user=user)
            response, code = leave_room(room, player)
            return Response(response, status=code)
        except (Room.DoesNotExist, User.DoesNotExist):
            return Response({'error': 'Комната или пользователь не найдены'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Получение сведений о комнате по ID',
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
        description='Обновление части данных комнаты',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление комнаты',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Комната удалена успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Комната не найдена',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)