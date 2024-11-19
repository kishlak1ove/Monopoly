from django.http import JsonResponse
from rest_framework import status

from ..models import Game, Room, Realty
from .controller_realty import ControllerRealty


class ControllerGame:
    @staticmethod
    def create(room):
        game = Game.objects.create(
            room=room,
            gametime=30,
            steptime=15
        )
        return game

    @staticmethod
    def create_realtys(game):
        price=500
        for i in range(1,32):
            if i % 4 == 0:
                continue
            realty = ControllerRealty.create(
                game=game,
                name='Недвижимость ' + str(i),
                price=price,
                position=i,
                rent=price*0.1
            )
            price += 500
            if realty is None:
                return JsonResponse({'error':'Недвижимость не создана', 'realty_id': i}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'Недвижимости созданы'}, status=status.HTTP_200_OK)

    @staticmethod
    def get_realtys(game):
        return ControllerRealty.get(game)

    @staticmethod
    def update(game):
        pass

    @staticmethod
    def delete(game):
        game.delete()
        return JsonResponse({'message':'Игра удалена'}, status=status.HTTP_204_NO_CONTENT)