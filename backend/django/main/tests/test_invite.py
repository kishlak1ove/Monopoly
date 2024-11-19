import pytest
import json
from rest_framework import status

from ..controllers.controller_invite import ControllerInvite
from ..controllers.controller_room import ControllerRoom
from ..models import Invite
from usermanager.models import User

@pytest.fixture
def testuser():
    return User.objects.create_user(username='testuser', email='test@example.com', password='psswrd')

@pytest.fixture
def testroom(testuser):
    return ControllerRoom.create(testuser)

@pytest.fixture
def testinvite(testuser, testroom):
    return ControllerInvite.create(testroom, testuser)

@pytest.mark.django_db
def test_invite_accepted(testinvite, testuser, testroom):
    response = ControllerInvite.accepted(testinvite)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode('utf-8'))
    assert data.get('invite_status') == Invite.Status.accepted

@pytest.mark.django_db
def test_invite_denied(testinvite, testuser, testroom):
    response = ControllerInvite.denied(testinvite)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = json.loads(response.content.decode('utf-8'))
    assert data.get('invite_status') == Invite.Status.declined
