from rest_framework import viewsets, status
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse

from ..serializers import RoomSerializer
from ..models import Room

@extend_schema(tags=['Room'], methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @extend_schema(
        description='Создание комнаты',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Комната создана',
                response=serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    @extend_schema(
        description='Список всех существующих комнат',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class(many=True)
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)

    @extend_schema(
        description='Получение сведений о комнате по ID',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description = 'Комната не найдена'
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description='Обновление комнаты',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_400_BAD_REQUEST: OpenApiResponse(
                description='Bad request'
            )
        }
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        description='Обновление части данных комнаты',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление комнаты',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Комната удалена успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Комната не найдена',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)