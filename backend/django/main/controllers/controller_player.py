from rest_framework import status

from .controller_realty import *
from ..models import Player, Realty, Room

def get_player(id):
    return Player.objects.get(id=id)

def create_player(user, room):
    player = Player.objects.create(
        user=user,
        room=room,
        score=3000,
        position=0,
        figure='Hat',
        is_arrested=False
    )
    return player

def delete_player(player):
    if not Player.objects.get(id=player.id):
        return {'error': 'Игрок не найден'}, status.HTTP_404_NOT_FOUND
    player.delete()
    return {'message': 'Игрок удалён'}, status.HTTP_204_NO_CONTENT

def move_player(player):
    import random
    steps = random.randint(1, 6)
    player.position = (player.position + steps) % 32
    player.save()
    if player.position in [4, 20]:
        arrest_player(player)
    return {'steps': steps, 'player_pos': player.position, 'is_arrested': player.is_arrested}, status.HTTP_200_OK

def buy_realty(realty, player):
    if player.score <= realty.price:
        return {'message': 'Недостаточно средств'}, status.HTTP_400_BAD_REQUEST
    response, code = set_owner(realty, player)
    if code == status.HTTP_400_BAD_REQUEST:
        return response, code
    player.score -= realty.price
    return {'message': 'Покупка недвижимости прошла успешно', 'balance': player.score}, status.HTTP_200_OK

def sell_realty(realty, player):
    player.score += realty.price
    response, code = delete_owner(realty)
    if code == status.HTTP_400_BAD_REQUEST:
        return response, code
    player.save()
    return {'message': 'Продажа недвижимости прошла успешно', 'balance': player.score}, status.HTTP_200_OK

def arrest_player(player):
    player.is_arrested = True
    player.position = 16
    player.save()
    return {'message': 'Игрок арестован'}, status.HTTP_200_OK
def unarrest_player(player):
    player.is_arrested = False
    player.save()
    return {'message': 'Игрок освобождён'}, status.HTTP_200_OK
