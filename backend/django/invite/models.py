from django.db import models
from datetime import datetime, timedelta

from usermanager.models import User
from room.models import Room

# Приглашение в комнату
class Invite(models.Model):
    class Status(models.TextChoices):
        waiting = "ожидает ответа", "Ожидает ответа"
        accepted = "принят", "Принят"
        declined = "отклонён", "Отклонён"

    # Статус, комната, игрок
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.waiting)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)