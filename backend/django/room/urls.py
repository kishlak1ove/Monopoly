from django.urls import path, include
from rest_framework import routers

from .views import RoomViewSet

router = routers.SimpleRouter()
router.register(r'room', RoomViewSet)

urlpatterns = [
    path('', include(router.urls))
]