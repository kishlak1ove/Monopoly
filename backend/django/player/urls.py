from django.urls import path, include
from rest_framework import routers

from .views import PlayerViewSet

router = routers.SimpleRouter()
router.register(r'player', PlayerViewSet)

urlpatterns = [
    path('', include(router.urls))
]