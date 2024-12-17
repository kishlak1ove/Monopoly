from django.db import models

from game.models import Game
from player.models import Player

# Недвижимость
class Realty(models.Model):
    # Игра, аренда, номер на игровом поле, наименование недвижимости, владелец, стоимость
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rent = models.IntegerField()
    position = models.IntegerField()
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Player, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name