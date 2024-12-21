from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse

from usermanager.models import User
from player.controllers import *
from player.serializers import PlayerSerializer
from .models import Player
from room.models import Room
from realty.models import Realty

@extend_schema(tags=['Player'])
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @extend_schema(
        description='Создание игрока',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Игрок создан',
                response=serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def create(self, request, *args, **kwargs):
        user = request.user
        room_id = request.data.get('room')
        try:
            room = Room.objects.get(pk=room_id)
            response = create_player(user, room)
            data = self.get_serializer(response).data
            return Response(data, status=status.HTTP_201_CREATED)
        except (User.DoesNotExist, Room.DoesNotExist):
            return Response({'error':'Пользователи или комната не найдены'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Движение игрока'
    )
    @action(methods=['patch'], detail=True)
    def move(self, request, *args, **kwargs):
        user = request.user
        try:
            player = Player.objects.filter(user=user).first()
            response, code = move_player(player)
            return Response(response, status=code)
        except (Player.DoesNotExist):
            return Response({'error':'Игрок не найден'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Покупка недвижимости игроком'
    )
    @action(methods=['patch'], detail=True)
    def buy(self, request, *args, **kwargs):
        player_id = kwargs.get('pk')
        realty_id = request.data.get('realty')
        try:
            player = Player.objects.get(id=player_id)
            realty = Realty.objects.get(id=realty_id)
            response, code = buy_realty(realty, player)
            return Response(response, status=code)
        except (Player.DoesNotExist, Realty.DoesNotExist):
            return Response({'error': 'Игрок или недвижимость не найдены'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Покупка недвижимости игроком'
    )
    @action(methods=['patch'], detail=True)
    def sell(self, request, *args, **kwargs):
        player_id = kwargs.get('pk')
        realty_id = request.data.get('realty')

        try:
            player = Player.objects.get(id=player_id)
            realty = Realty.objects.get(id=realty_id)
            response, code = sell_realty(realty, player)
            return Response(response, status=code)
        except (Player.DoesNotExist, Realty.DoesNotExist):
            return Response({'error': 'Игрок или недвижимость не найдены'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Освобождение игрока из тюрьмы'
    )
    @action(methods=['patch'], detail=True)
    def unarrest(self, request, *args, **kwargs):
        player_id = kwargs.get('pk')
        print(player_id)
        try:
            player = Player.objects.get(id=player_id)
            response, code = unarrest_player(player)
            return Response(response, status=code)
        except (Player.DoesNotExist):
            return Response({'error': 'Игрок не найден'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Список всех существующих игроков',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class(many=True)
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)

    @extend_schema(
        description='Получение сведений об игроке по ID',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description = 'Игрок не найден'
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description='Обновление игрока',
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
        description='Обновление части данных игрока',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление игрока',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Игрок удален успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Игрок не найден',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)