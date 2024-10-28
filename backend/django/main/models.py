from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Игрок
class Player(models.Model):
    # пользователь, имя, счёт, позиция, фигура, под арестом ли
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
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

# Карточка "Шанс"
class Chance(models.Model):
    class Effect(models.TextChoices):
        increase_500 = 'прибыль_500', 'Прибыль_500'
        increase_1000 = 'прибыль_1000', 'Прибыль_1000'
        decrease_500 = 'штраф_500', 'Штраф_500'

    effect = models.CharField(max_length=20, choices=Effect.choices)

    def apply_to_player(self, player: Player):
        # Применяет эффект карточки к игроку
        if self.effect == self.Effect.INCREASE_500:
            player.score += 500
        elif self.effect == self.Effect.INCREASE_1000:
            player.score += 1000
        elif self.effect == self.Effect.DECREASE_500:
            player.score -= 500
        player.save()

# Игровая доска
class Board(models.Model):
    # игра, список недвижимостей, список карточек "Шанс"
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    realty = models.ManyToManyField(Realty, blank=True)
    chance = models.ManyToManyField(Chance, blank=True)
