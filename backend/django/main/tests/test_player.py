import pytest
import json
from rest_framework.test import APIClient
from rest_framework import status

from usermanager.models import User
from ..models import Player
from ..controllers.controller_player import *
from ..controllers.controller_room import *
from ..controllers.controller_game import *
from ..controllers.controller_realty import *

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def testuser():
    return User.objects.create_user(username='testuser', email='test@example.com', password='psswrd')

@pytest.fixture
def testroom(testuser):
    return ControllerRoom.create(testuser)

@pytest.fixture
def testgame(testroom):
    return ControllerGame.create(testroom)

@pytest.fixture
def testplayer(testuser, testroom):
    return ControllerPlayer.create(testuser, testroom)

@pytest.fixture
def testrealty(testgame):
    return ControllerRealty.create(game=testgame, name='Test', price=1000, position=0, rent=100)

@pytest.mark.django_db
def test_create_player(testuser, testroom):
    player = ControllerPlayer.create(testuser, testroom)
    assert player is not None
    assert player.room == testroom
    assert player.user == testuser
    assert player.score == 3000
    assert player.position == 0
    assert player.is_arrested == False
    assert player.figure == 'Hat'

@pytest.mark.django_db
def test_player_move(testplayer):
    response = ControllerPlayer.move(testplayer)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = response.content.decode('utf-8')
    data = json.loads(data)
    print(data)
    assert data.get('player_pos') == testplayer.position
    assert data.get('steps')

@pytest.mark.django_db
def test_player_buy(testplayer, testgame, testrealty):
    response = ControllerPlayer.buy(testplayer, testgame)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = response.content.decode('utf-8')
    data = json.loads(data)
    assert data.get('balance') == testplayer.score

@pytest.mark.django_db
def test_player_sell(testplayer, testrealty):
    response = ControllerPlayer.sell(testplayer, testrealty)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = response.content.decode('utf-8')
    data = json.loads(data)
    assert data.get('balance') == testplayer.score

@pytest.mark.django_db
def test_player_unarrest(testplayer):
    testplayer.is_arrested = True
    response = ControllerPlayer.unarrest(testplayer)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    assert testplayer.is_arrested == False

