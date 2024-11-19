from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from ..models import Room, Player

class ControllerRoom:

    @staticmethod
    def create(user):
        room = Room.objects.create(
            status=Room.Status.incomplete,
            name='Room ' + str(user.id),
            admin=user,
            init_score=3000,
            is_private=True,
            player_count=4
        )
        return room

    @staticmethod
    def update(room, name, init_score, is_private, player_count):
        if Room.objects.filter(name=name).exists():
            return JsonResponse({'message': 'Комната с таким именем существует'}, status=status.HTTP_400_BAD_REQUEST)
        if init_score < 0:
            return JsonResponse({'message': 'Начальная сумма денег не может быть отрицательной'}, status=status.HTTP_400_BAD_REQUEST)
        if player_count > 4:
            return JsonResponse({'message': 'В комнате может быть не больше 4 игроков'}, status=status.HTTP_400_BAD_REQUEST)
        if player_count < 2:
            return JsonResponse({'message': 'Минимум нужно 2 игрока'}, status=status.HTTP_400_BAD_REQUEST)
        room.name = name
        room.init_score = init_score
        room.is_private = is_private
        room.player_count = player_count
        room.save()
        return JsonResponse({'message': 'Данные обновлены'}, status=status.HTTP_200_OK)

    @staticmethod
    def delete(room):
        room.delete()
        return JsonResponse({'message': 'Комната расформирована'}, status=status.HTTP_204_NO_CONTENT)

