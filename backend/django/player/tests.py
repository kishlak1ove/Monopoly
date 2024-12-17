import pytest
from rest_framework.test import APIClient

from usermanager.models import User
from backend.django.main.models import Game
from backend.django.room.controllers import *
from backend.django.realty.controllers import *

@pytest.fixture
def client():
    return APIClient()

# @pytest.fixture(autouse=True)
# def clear_database(db):
#     Player.objects.all().delete()

@pytest.fixture
def testuser():
    return User.objects.create_user(username='testuser', email='test@example.com', password='psswrd')

@pytest.fixture
def testroom(testuser):
    return create_room(testuser)

@pytest.fixture
def testgame(testroom):
    return Game.objects.create(
        gametime=30,
        steptime=30,
        room=testroom,
        is_active=True
    )

@pytest.fixture
def testplayer(testuser, testroom):
    return create_player(testuser, testroom)

@pytest.fixture
def testrealtys(testgame):
    return create_realtys(game=testgame)

@pytest.mark.django_db
def test_create_player(client, testuser, testroom):
    url = '/api/v1/player/'
    data = {
        'room': testroom.id
    }
    client.force_authenticate(testuser)
    response = client.post(url, data, format='json')
    assert response is not None
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert 'id' in data
    assert 'score'in data
    assert 'position' in data
    assert 'is_arrested' in data
    assert 'figure' in data

@pytest.mark.django_db
def test_player_move(client, testuser, testplayer):
    url = f'/api/v1/player/{testplayer.id}/move/'

    client.force_authenticate(user=testuser)
    response = client.patch(url)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    if data.get('is_arrested'):
        assert data.get('player_pos') == 16
    else:
        assert data.get('player_pos') == testplayer.position + data.get('steps')

@pytest.mark.django_db
def test_player_buy(client, testuser, testplayer, testrealtys):
    url = f'/api/v1/player/{testplayer.id}/buy/'
    data = {
        'realty': testrealtys[0].id
    }

    client.force_authenticate(user=testuser)
    response = client.patch(url, data, format='json')
    assert response is not None
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data.get('message') == 'Покупка недвижимости прошла успешно'

@pytest.mark.django_db
def test_player_buy_extists_owner(client, testuser, testplayer, testrealtys):
    url = f'/api/v1/player/{testplayer.id}/buy/'
    data = {
        'realty': testrealtys[0].id
    }

    testrealtys[0].owner = testplayer
    testrealtys[0].save()
    client.force_authenticate(user=testuser)
    response = client.patch(url, data, format='json')
    assert response is not None
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert data.get('message') == 'Этой недвижимостью владеет другой игрок'

@pytest.mark.django_db
def test_player_sell(client, testuser, testplayer, testrealtys):
    url = f'/api/v1/player/{testplayer.id}/sell/'
    data = {
        'realty': testrealtys[0].id
    }
    testrealtys[0].owner = testplayer
    testrealtys[0].save()

    client.force_authenticate(user=testuser)
    response = client.patch(url, data, format='json')
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data.get('message') == 'Продажа недвижимости прошла успешно'

@pytest.mark.django_db
def test_player_unarrest(client, testuser, testplayer):
    url = f'/api/v1/player/{testplayer.id}/unarrest/'
    testplayer.is_arrested = True

    client.force_authenticate(user=testuser)
    response = client.patch(url)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data.get('message') == 'Игрок освобождён'

