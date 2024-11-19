from rest_framework import viewsets, status
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse

from ..serializers import InviteSerializer
from ..models import Invite

@extend_schema(tags=['Invite'], methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
class InviteViewSet(viewsets.ModelViewSet):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    @extend_schema(
        description='Создание приглашения',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Приглашение создано',
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
        description='Список всех существующих приглашений',
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
        description='Получение сведений о приглашении по ID',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description = 'Приглашение не найдено'
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description='Обновление приглашения',
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
        description='Обновление части данных приглашения',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление приглашения',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Приглашение удалено успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Приглашение не найдено',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)