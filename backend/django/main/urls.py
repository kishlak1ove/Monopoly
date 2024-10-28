from django.urls import path, include, re_path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import permissions

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
    path('schema/', CoreSpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),

    path('', include(router_room.urls)),
    path('', include(router_player.urls)),
    path('', include(router_board.urls)),
    path('', include(router_game.urls)),
    path('', include(router_realty.urls)),
    path('', include(router_invite.urls)),
]