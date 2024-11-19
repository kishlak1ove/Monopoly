from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import register_view, login_view, logout_view, UserViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
]