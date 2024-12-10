from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from .controller_player import *
from ..models import Room, Player

def create_room(user):
    room = Room.objects.create(
        status=Room.Status.incomplete,
        name='Room ' + str(user.id),
        admin=user,
        init_score=3000,
        is_private=True,
        player_count=4
    )
    create_player(user, room)
    return room

def join_to_room(room, user):
    players = Player.objects.filter(room=room)
    if players.count() > 3:
        return {'error': 'Комната заполнена'}, status.HTTP_400_BAD_REQUEST
    player = create_player(user, room)
    if player is not None:
        return {'message': 'Игрок присоединился к комнате'}, status.HTTP_200_OK

def leave_room(room, player):
    if not Player.objects.get(id=player.id):
        return {'error': 'Игрок не найден'}, status.HTTP_400_BAD_REQUEST
    if player.room != room:
        return {'error': 'Игрок не состоит в комнате'}, status.HTTP_400_BAD_REQUEST
    delete_player(player)
    return {'message': 'Игрок покинул комнату и был удалён'}, status.HTTP_200_OK

def update_room(room, stat, name, init_score, is_private, player_count):
    if Room.objects.filter(name=name).exists():
        return {'message': 'Комната с таким именем существует'}, status.HTTP_400_BAD_REQUEST
    if player_count > 4:
        return {'message': 'В комнате может быть не больше 4 игроков'}, status.HTTP_400_BAD_REQUEST
    if player_count < 2:
        return {'message': 'Минимум нужно 2 игрока'}, status.HTTP_400_BAD_REQUEST
    room.name = name
    room.status = stat
    room.init_score = init_score
    room.is_private = is_private
    room.player_count = player_count
    room.save()
    return {
        'message': 'Данные обновлены',
        'room': {
            'status': room.status,
            'name': room.name,
            'init_score': room.init_score,
            'is_private': room.is_private,
            'player_count': room.player_count
        }
    }, status.HTTP_200_OK

def delete_room(room):
    if not Room.objects.get(id=room.id):
        return {'error': 'Комната не найдена'}, status.HTTP_400_BAD_REQUEST
    room.delete()
    return {'message': 'Комната расформирована'}, status.HTTP_204_NO_CONTENT
