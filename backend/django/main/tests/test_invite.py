import pytest
import json
from rest_framework.test import APIClient
from rest_framework import status

from ..controllers.controller_invite import *
from ..controllers.controller_room import *
from ..models import Invite
from usermanager.models import User

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def testuser():
    return User.objects.create_user(username='testuser', email='test@example.com', password='psswrd')

@pytest.fixture
def testroom(testuser):
    return create_room(testuser)

@pytest.fixture
def testinvite(testuser, testroom):
    return create_invite(testroom, testuser)

@pytest.mark.django_db
def test_invite_accepted(client, testinvite, testuser, testroom):
    url = f'/api/v1/invite/{testinvite.id}/accept/'

    client.force_authenticate(testuser)
    response = client.get(url)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data.get('invite_status') == Invite.Status.accepted

@pytest.mark.django_db
def test_invite_denied(client, testinvite, testuser, testroom):
    url = f'/api/v1/invite/{testinvite.id}/denied/'

    client.force_authenticate(testuser)
    response = client.get(url)
    assert response is not None
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data.get('invite_status') == Invite.Status.declined
