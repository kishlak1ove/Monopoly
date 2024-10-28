from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Игрок
class Player(models.Model):
    # пользователь, имя, счёт, позиция, фигура, под арестом ли
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    score = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    figure = models.CharField(max_length=150)
    is_arrested = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# Комната
class Room(models.Model):
    class Status(models.TextChoices):
        full = "заполнен", "Заполнен"
        incomplete = "есть места", "Есть места"

    # Статус, администратор комнаты, имя комнаты, закрытая ли комната, кол-во игроков, список игроков в комнате
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.incomplete)
    admin = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='admin_rooms')
    name = models.CharField(max_length=160, blank=True)
    init_score = models.IntegerField(default=3000)
    is_private = models.BooleanField(default=False)
    player_count = models.IntegerField(default=1)
    players = models.ManyToManyField(Player, blank=True, related_name='players_rooms')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.admin.name}'s room"
        super().save(*args, **kwargs)

    def clean(self):
        err = ""
        if self.player_count > 3:
            err += "В комнате может быть не более 3 игроков."
        elif self.player_count < 1:
            err += "Для игры нужен ещё один игрок."
        if self.init_score < 1000:
            err += "Начальная сумма не может быть меньше 1000."
        if err:
            raise ValidationError(err)

    def __str__(self):
        return self.name

# Приглашение в комнату
class Invite(models.Model):
    class Status(models.TextChoices):
        waiting = "ожидает ответа", "Ожидает ответа"
        accepted = "принят", "Принят"
        declined = "отклонён", "Отклонён"

    # Статус, комната, игрок
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.waiting)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

# Недвижимость
class Realty(models.Model):
    # Аренда, наименование недвижимости, владелец, стоимость
    rent = models.IntegerField()
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

# Игра
class Game(models.Model):
    # время игры, комната, список недвижимостей
    gametime = models.FloatField(default=30)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    realty = models.ManyToManyField(Realty, blank=True)
