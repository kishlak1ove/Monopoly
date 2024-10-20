from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=150)
    position = models.IntegerField()
    figure = models.CharField(max_length=150)

class Room(models.Model):
    status = models.CharField(max_length=16)
    admin = models.OneToOneField(Player, on_delete=models.CASCADE)
    name = models.CharField(max_length=160, default=f"{admin.name}'s room")
    is_private = models.BooleanField(default=False)
    player_count = models.IntegerField(default=2)

class Invite(models.Model):
    status = models.CharField(max_length=16)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Game(models.Model):
    gametime = models.FloatField()
    steptime = models.FloatField(default=0, null=True)
    step_count = models.IntegerField(default=10, null=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)

class Board(models.Model):
    fields = models.CharField(max_length=1024)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)

class Prison(models.Model):
    deposit = models.IntegerField(default=250)

class Realty(models.Model):
    rent = models.IntegerField()
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

class Chance(models.Model):
    descrioption = models.CharField(max_length=1024)
