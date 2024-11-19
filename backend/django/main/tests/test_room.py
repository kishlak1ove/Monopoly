import pytest
import json
from rest_framework import status

from ..models import Room
from ..controllers.controller_room import *
from usermanager.models import User

@pytest.fixture
def testuser():
    return User.objects.create_user(username='testuser', email='test@example.com', password='psswrd')

@pytest.fixture
def testroom(testuser):
    return ControllerRoom.create(testuser)

@pytest.mark.django_db
def test_create_room(testuser):
    room = ControllerRoom.create(testuser)
    assert room is not None
    assert room.name == 'Room 1'
    assert room.status == Room.Status.incomplete
    assert room.init_score == 3000
    assert room.player_count == 4
    assert room.is_private == True

@pytest.mark.django_db
def test_update_room_invalid_var(testuser, testroom):
    response = ControllerRoom.update(testroom, name='Test', init_score=-1, player_count=2, is_private=False)
    assert response is not None
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    data = json.loads(response.content.decode('utf-8'))
    assert data.get('message') == 'Начальная сумма денег не может быть отрицательной'
