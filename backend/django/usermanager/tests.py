import pytest
from rest_framework.test import APIClient
from rest_framework import status

from .models import User

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def create_test_user():
    user = User.objects.create_user(username="testuser", email="test@example.ru", password="psswrd")
    return user

@pytest.mark.django_db
def test_user_creation(client):
    url = '/api/v1/register/'
    data = {
        'username': 'testuser',
        'email': 'test@example.ru',
        'password': 'psswrd'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='testuser').exists()
#
@pytest.mark.django_db
def test_user_creation_exists(client, create_test_user):
    url = '/api/v1/register/'
    data = {
        'username': 'testuser',
        'email': 'test@example.ru',
        'password1': 'psswrd'
    }
    response = client.post(url, data, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_user_login(client, create_test_user):
    '''Тест на авторизацию пользователя'''
    url = '/api/v1/login/'
    data = {
        'username': 'testuser',
        'password': 'psswrd'
    }
    response = client.post(url, data, format='json')
    assert response.json().get('message') == 'Success'
    assert response.status_code == status.HTTP_200_OK

@pytest.mark.django_db
def test_user_login_failed(client):
    '''Тест на авторизацию пользователя с неверными данными'''
    url = '/api/v1/login/'
    data = {
        'username': 'testuser',
        'password': 'pssd'
    }
    response = client.post(url, data, format='json')
    assert response.json().get('message') == 'Неверный логин или пароль'
    assert response.status_code == status.HTTP_400_BAD_REQUEST

