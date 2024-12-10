from rest_framework import status

from ..models import Invite, Player
from .controller_room import *

def create_invite(room, user):
    if Invite.objects.filter(room=room, user=user).exists():
        return {'error': 'Приглашение уже создано'}, status.HTTP_400_BAD_REQUEST
    invite = Invite.objects.create(room=room, user=user, status=Invite.Status.waiting)
    return invite

def accept_invite(invite):
    _, code = join_to_room(room=invite.room, user=invite.user)
    if code != status.HTTP_200_OK:
        return {'error': 'Игрок не был создан'}, status.HTTP_400_BAD_REQUEST
    invite.status = Invite.Status.accepted
    invite.save()
    return {'message':'Приглашение принято', 'invite_status': invite.status}, status.HTTP_200_OK

def denied_invite(invite):
    invite.status = Invite.Status.declined
    invite.save()
    return {'message':'Приглашение отклонено', 'invite_status': invite.status}, status.HTTP_200_OK

def delete_invite(invite):
    invite.delete()
    return {'message':'Приглашение удалено'}, status.HTTP_200_OK
