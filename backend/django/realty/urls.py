from django.urls import path, include
from rest_framework import routers

from .views import RealtyViewSet

router = routers.SimpleRouter()
router.register(r'realty', RealtyViewSet)

urlpatterns = [
    path('', include(router.urls))
]