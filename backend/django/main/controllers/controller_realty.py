from django.http import JsonResponse
from rest_framework import status
from django.db.models import SET_NULL

from ..models import Realty

class ControllerRealty:
    @staticmethod
    def create(game, name, price, position, rent):
        realty = Realty.objects.create(
            game=game,
            name=name,
            price=price,
            position=position,
            rent=rent
        )
        return realty

    @staticmethod
    def get(game):
        return Realty.objects.filter(game=game)

    @staticmethod
    def set_owner(realty, player):
        realty.owner = player
        realty.save()
        return JsonResponse({'message': 'Владелец установлен'}, status=status.HTTP_200_OK)

    @staticmethod
    def delete_owner(realty):
        realty.owner = None
        realty.save()
        return JsonResponse({'message': 'Владелец удалён'}, status=status.HTTP_200_OK)

    @staticmethod
    def delete(realty):
        realty.delete()
        return JsonResponse({'message':'Недвижимость удалена'}, status=status.HTTP_204_NO_CONTENT)