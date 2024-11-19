from django.db import models

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
    init_score = models.IntegerField(default=3000)
    is_private = models.BooleanField(default=False)
    player_count = models.IntegerField(default=4)

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"{self.admin.name}'s room"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

# Игрок
class Player(models.Model):
    # пользователь, имя, счёт, позиция, фигура, под арестом ли
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    position = models.IntegerField(default=0)
    figure = models.CharField(max_length=150)
    is_arrested = models.BooleanField(default=False)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Игра
class Game(models.Model):
    # время игры, время хода, комната
    gametime = models.FloatField(default=30)
    steptime = models.FloatField(default=15)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


# Недвижимость
class Realty(models.Model):
    # Аренда, наименование недвижимости, владелец, стоимость
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rent = models.IntegerField()
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Player, on_delete=models.SET_NULL, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name
