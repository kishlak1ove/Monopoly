from rest_framework import status

from .models import Realty

# Недвижимости по дефолту будут иметь такие имена, цены и стоимость аренды.
# Возможно в дальнейшем сделаем для игроков возможность кастомизировать недвижимости
realtys_default = [
    # [name, position, price, rent]
    ['Автомат с жевательными резинками', 1, 500, 50],
    ['Тележка хот-догов', 2, 1000, 100],
    ['Фургон с мороженным', 3, 1500, 150],
    ['Кладовая', 5, 2000, 200],
    ['Контейнер', 6, 2500, 250],
    ['Студия 20 квм', 7, 3000, 300],
    ['Салон красоты', 9, 3500, 350],
    ['Тур-агентство', 10, 4000, 400],
    ['Продуктовый магазин', 11, 4500, 450],
    ['Магазин хозтоваров', 13, 5000, 500],
    ['Магазин алкогольной и табачной продукции', 14, 5500, 550],
    ['Магазин одежды', 15, 6000, 600],
    ['Мастерская по ремонту обуви', 17, 6500, 650],
    ['Ателье', 18, 7000, 700],
    ['Мастерская по ремонту бытовой техники', 19, 7500, 750],
    ['Магазин бытовой техники', 21, 8000, 800],
    ['Ювелирный магазин', 22, 8500, 850],
    ['Магазин универсал', 23, 9000, 900],
    ['Салон автомобилей Haval', 25, 9500, 950],
    ['Салон автомобилей Toyota', 26, 10000, 1000],
    ['Салон автомобилей Lada', 27, 10500, 1050],
    ['Акции компании Yandex', 29, 11000, 1100],
    ['Акции компании Газпром', 30, 11500, 1150],
    ['Акции компании Лукойл', 31, 12000, 1200]
]


def create_realtys(game):
    data = []
    for realty in realtys_default:
        re = Realty.objects.create(
            game=game,
            name=realty[0],
            position=realty[1],
            price=realty[2],
            rent=realty[3]
        )
        data.append(re)
    return data

def set_owner(realty, player):
    if realty.owner is not None:
        return {'message':'Этой недвижимостью владеет другой игрок'}, status.HTTP_400_BAD_REQUEST
    realty.owner = player
    realty.save()
    return {'message': 'Владелец установлен'}, status.HTTP_200_OK

def delete_owner(realty):
    realty.owner = None
    realty.save()
    return {'message': 'Владелец удалён'}, status.HTTP_200_OK

def list_realtys(game_id):
    return Realty.objects.filter(game=game_id)
    