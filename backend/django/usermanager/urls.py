from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import logout_view, LoginView, RegisterView, UserViewSet

router = SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/logout/', logout_view, name='logout'),
]