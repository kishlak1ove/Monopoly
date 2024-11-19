import pytest

from usermanager.models import User
from ..controllers.controller_realty import *
from ..controllers.controller_game import ControllerGame
from ..controllers.controller_room import ControllerRoom
from ..models import Realty

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
def testrealtys(testgame):
    return ControllerGame.create_realtys(testgame)

@pytest.mark.django_db
def test_realty_get(testrealtys, testgame):
    response = ControllerRealty.get(testgame)
    assert (testrealtys == realty for realty in response)
