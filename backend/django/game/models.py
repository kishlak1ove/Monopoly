from django.db import models
from datetime import datetime, timedelta

from room.models import Room


# Игра
class Game(models.Model):
    gametime = models.FloatField(default=30)
    steptime = models.FloatField(default=15)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Game in {self.room.name}"

    def calculate_end_time(self):
        if self.start_time:
            return self.start_time + timedelta(minutes=self.gametime)
        return None

    def is_time_over(self):
        if self.end_time:
            return datetime.now() >= self.end_time
        if self.start_time:
            return datetime.now() >= self.calculate_end_time()
        return False
