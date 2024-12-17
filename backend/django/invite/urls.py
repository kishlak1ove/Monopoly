from django.urls import path, include
from rest_framework import routers

from .views import InviteViewSet

router = routers.SimpleRouter()
router.register(r'invite', InviteViewSet)

urlpatterns = [
    path('', include(router.urls))
]