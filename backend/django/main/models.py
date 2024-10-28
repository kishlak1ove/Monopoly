from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Игрок
class Player(models.Model):
    # пользователь, имя, счёт, позиция, фигура, под арестом ли
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    score = models.IntegerField(default=5000)
    position = models.IntegerField(default=0)
    figure = models.CharField(max_length=150)
    is_arrested = models.BooleanField(default=False)

# Комната
class Room(models.Model):
    # Статус, администратор комнаты, имя комнаты, закрытая ли комната, кол-во игроков, список игроков в комнате
    status = models.CharField(max_length=16)
    admin = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='admin_rooms')
    name = models.CharField(max_length=160, blank=True)
    is_private = models.BooleanField(default=False)
    player_count = models.IntegerField(default=1)
    players = models.ManyToManyField(Player, blank=True, related_name='players_rooms')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.admin.name}'s room"
        super().save(*args, **kwargs)

    def clean(self):
        if self.player_count > 3:
            raise ValidationError("В комнате может быть не более 3 игроков")
        if self.player_count < 1:
            raise ValidationError("Для игры нужен ещё один игрок")

# Приглашение в комнату
class Invite(models.Model):
    # Статус, комната, игрок
    status = models.CharField(max_length=16)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

# Игра
class Game(models.Model):
    # время игры, время хода, кол-во ходов, комната
    gametime = models.FloatField(blank=True, null=True)
    steptime = models.FloatField(default=0, blank=True ,null=True)
    step_count = models.IntegerField(default=10, blank=True ,null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

# Недвижимость
class Realty(models.Model):
    # Аренда, наименование недвижимости, владелец, стоимость
    rent = models.IntegerField()
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()

# Игровая доска
class Board(models.Model):
    # игра, список недвижимостей
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    realty = models.ManyToManyField(Realty, blank=True)
