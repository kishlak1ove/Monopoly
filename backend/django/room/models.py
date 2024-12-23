from django.db import models
from datetime import datetime, timedelta

from usermanager.models import User


# Комната
class Room(models.Model):
    class Status(models.TextChoices):
        full = "заполнен", "Заполнен"
        incomplete = "есть места", "Есть места"

    # Статус, администратор комнаты, имя комнаты, закрытая ли комната, кол-во игроков, список игроков в комнате
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.incomplete)
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_rooms')
    name = models.CharField(max_length=160, blank=True)
    init_score = models.PositiveIntegerField(default=3000)
    is_private = models.BooleanField(default=True)
    player_count = models.PositiveIntegerField(default=4)
    gametime = models.FloatField(default=30)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.admin.username}'s room"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name