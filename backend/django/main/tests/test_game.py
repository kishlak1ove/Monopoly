import pytest
from rest_framework.test import APIClient
from rest_framework import status

from ..controllers.controller_game import *
from ..models import Game

@pytest.fixture
def client():
    return APIClient()

@pytest.mark.django_db
def test_game():
    pass

