from rest_framework.routers import SimpleRouter

from .views import *

router_room = SimpleRouter()
router_room.register(r'room', RoomViewSet, )

router_player = SimpleRouter()
router_player.register(r'player', PlayerViewSet, )

router_game = SimpleRouter()
router_game.register(r'game', GameViewSet, )

router_board = SimpleRouter()
router_board.register(r'board', BoardViewSet, )

router_realty = SimpleRouter()
router_realty.register(r'realty', RealtyViewSet, )

router_invite = SimpleRouter()
router_invite.register(r'invite', InviteViewSet, )