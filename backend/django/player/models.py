from django.db import models
from datetime import datetime, timedelta

from usermanager.models import User
from room.models import Room

# Игрок
class Player(models.Model):
    # пользователь, имя, счёт, позиция, фигура, под арестом ли
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    score = models.IntegerField(default=3000)
    position = models.IntegerField(default=0)
    figure = models.CharField(max_length=150)
    is_arrested = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username