from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import permissions

from .views import *
from .routers import *

class CoreSpectacularAPIView(SpectacularAPIView):
    custom_settings = {
        'TITLE': 'Admin API',
        'SCHEMA_PATH_PREFIX': '/api/v1/',
        'DESCRIPTION': 'Для администрирования',
        'VERSION': '1.0.0'
    }
    patterns = [
        re_path(r'^api/v1/', include('main.urls')),
    ]
    permission_classes = [permissions.AllowAny,]
    serve_public = True


urlpatterns = [
    path('schema/', CoreSpectacularAPIView.as_view(), name='init_schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='init_schema'), name='init_swagger'),

    path('Room/', include(router_Room.urls)),
    path('Player/', include(router_Player.urls)),
    path('Board/', include(router_Board.urls)),
    path('Game/', include(router_Game.urls)),
    path('Chance/', include(router_Chance.urls)),
    path('Prison/', include(router_Prison.urls)),
    path('Realty/', include(router_Realty.urls)),
    path('Invite/', include(router_Invite.urls)),

]