from rest_framework.routers import SimpleRouter

from main.views import RoomViewSet, PlayerViewSet, GameViewSet, BoardViewSet, ChanceViewSet, PrisonViewSet, \
    RealtyViewSet, InviteViewSet

router_Room = SimpleRouter()
router_Room.register(r'Room', RoomViewSet, )

router_Player = SimpleRouter()
router_Player.register(r'Player', PlayerViewSet, )

router_Game = SimpleRouter()
router_Game.register(r'Game', GameViewSet, )

router_Board = SimpleRouter()
router_Board.register(r'Board', BoardViewSet, )

router_Chance = SimpleRouter()
router_Chance.register(r'Chance', ChanceViewSet, )

router_Prison = SimpleRouter()
router_Prison.register(r'Prison', PrisonViewSet, )

router_Realty = SimpleRouter()
router_Realty.register(r'Realty', RealtyViewSet, )

router_Invite = SimpleRouter()
router_Invite.register(r'Invite', InviteViewSet, )