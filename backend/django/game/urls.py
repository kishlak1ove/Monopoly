from django.urls import path, include
from rest_framework import routers

from .views import GameViewSet

router = routers.SimpleRouter()
router.register(r'game', GameViewSet)

urlpatterns = [

    path('', include(router.urls)),
]