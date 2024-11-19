from django.http import JsonResponse
from rest_framework import status

from ..models import Invite, Player
from .controller_player import ControllerPlayer
class ControllerInvite:
    @staticmethod
    def create(room, user):
        invite = Invite.objects.create(room=room, user=user, status=Invite.Status.waiting)
        return invite

    @staticmethod
    def accepted(invite):
        player = ControllerPlayer.create(user=invite.user, room=invite.room)
        if player is None:
            return JsonResponse({'error': 'Игрок не был создан'}, status=status.HTTP_400_BAD_REQUEST)
        invite.status = Invite.Status.accepted
        invite.save()
        return JsonResponse({'message':'Приглашение принято', 'invite_status': invite.status}, status=status.HTTP_200_OK)

    @staticmethod
    def denied(invite):
        invite.status = Invite.Status.declined
        invite.save()
        return JsonResponse({'message':'Приглашение отклонено', 'invite_status': invite.status}, status=status.HTTP_200_OK)

    @staticmethod
    def delete(invite):
        invite.delete()
        return JsonResponse({'message':'Приглашение удалено'}, status=status.HTTP_204_NO_CONTENT)
