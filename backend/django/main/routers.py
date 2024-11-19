from rest_framework.routers import SimpleRouter

from .views.view_game import GameViewSet
from .views.view_invite import InviteViewSet
from .views.view_player import PlayerViewSet
from .views.view_room import RoomViewSet
from .views.view_realty import RealtyViewSet

router = SimpleRouter()
router.register(r'room', RoomViewSet)
router.register(r'game', GameViewSet)
router.register(r'player', PlayerViewSet)
router.register(r'realty', RealtyViewSet)
router.register(r'invite', InviteViewSet)
