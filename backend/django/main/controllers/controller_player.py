from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import random

from .controller_realty import ControllerRealty
from ..models import Player, Realty, Room

class ControllerPlayer:
    @staticmethod
    def create(user, room):
        score = room.init_score
        player = Player.objects.create(
            user=user,
            room=room,
            score=score,
            position=0,
            figure='Hat',
            is_arrested=False
        )
        return player

    @staticmethod
    def move(player):
        steps = random.randint(1, 6)
        player.position = (player.position + steps) % 32
        player.save()
        return JsonResponse({'steps': steps, 'player_pos': player.position}, status=status.HTTP_200_OK)

    @staticmethod
    def buy(player, game):
        realty = Realty.objects.get(position=player.position,game=game)
        if player.score <= realty.price:
            return JsonResponse({'message': 'Недостаточно средств',}, status=status.HTTP_200_OK)
        response = ControllerRealty.set_owner(realty, player)
        if response.status_code != status.HTTP_200_OK:
            return JsonResponse({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        player.score -= realty.price
        return JsonResponse({'message': 'Покупка недвижимости прошла успешно', 'balance': player.score}, status=status.HTTP_200_OK)

    @staticmethod
    def sell(player, realty):
        player.score += realty.price
        response = ControllerRealty.delete_owner(realty)
        if response.status_code != status.HTTP_200_OK:
            return JsonResponse({'error':'Bad request'}, status=status.HTTP_400_BAD_REQUEST)
        player.save()
        return JsonResponse({'message': 'Продажа недвижимости прошла успешно', 'balance': player.score}, status=status.HTTP_200_OK)

    @staticmethod
    def unarrest(player):
        player.is_arrested = False
        player.save()
        return JsonResponse({'message': 'Игрок освобождён'}, status=status.HTTP_200_OK)
