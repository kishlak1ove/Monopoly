import pytest
from rest_framework.test import APIClient

from backend.django.main.models import Room
from backend.django.room.controllers import *
from usermanager.models import User

@pytest.fixture
def client():
    return APIClient()
@pytest.fixture
def testuser():
    return User.objects.create_user(
        username='testuser',
        email='test@example.com',
        password='psswrd'
    )

@pytest.fixture
def testroom(testuser):
    return create_room(testuser)

@pytest.fixture
def testusers():
    return [User.objects.create_user(username=f'testuser{i}', email=f'abc{i}@example.ru', password='123')
            for i in range(1,4)]

@pytest.mark.django_db
def test_create_room(client, testuser):
    url = '/api/v1/room/'

    client.force_authenticate(user=testuser)
    response = client.post(url)
    assert response.status_code == status.HTTP_201_CREATED
    data = response.json()
    assert 'status' in data
    assert 'name' in data
    assert 'admin' in data
    assert 'init_score' in data
    assert 'is_private' in data
    assert 'player_count' in data

@pytest.mark.django_db
def test_update_room_exists(client, testuser, testroom):
    url = f'/api/v1/room/{testroom.id}/'
    data = {
        'status': Room.Status.incomplete,
        'name': testroom.name,
        'init_score': 5000,
        'is_private': False,
        'player_count': 2
    }
    response = client.put(url, data, format='json')
    assert response is not None
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert data.get('message') == 'Комната с таким именем существует'

@pytest.mark.django_db
def test_join_room(client, testroom, testuser):
    url = f'/api/v1/room/{testroom.id}/join/'

    client.force_authenticate(testuser)
    response = client.get(url)

    assert response is not None
    assert response.status_code == status.HTTP_200_OK
    data = response.json()
    assert data.get('message') == 'Игрок присоединился к комнате'

@pytest.mark.django_db
def test_join_full_room(client, testuser, testroom, testusers):
    url = f'/api/v1/room/{testroom.id}/join/'

    for user in testusers:
        client.force_authenticate(user)
        client.get(url)
    client.force_authenticate(testuser)
    response = client.get(url)

    assert response is not None
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    data = response.json()
    assert data.get('error') == 'Комната заполнена'

@pytest.mark.django_db
def test_leave_room(client, testroom, testuser):
    url = f'/api/v1/room/{testroom.id}/leave/'

    client.force_authenticate(testuser)
    response = client.get(url)

    assert response is not None
    assert response.status_code == status.HTTP_200_OK

    data = response.json()
    assert data.get('message') == 'Игрок покинул комнату и был удалён'