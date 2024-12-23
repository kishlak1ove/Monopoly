from rest_framework import viewsets, status
from rest_framework.response import Response
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse
import json

from .serializers import RealtySerializer
from .models import Realty
from .controllers import *

@extend_schema(tags=['Realty'], methods=["GET", "POST", "PUT", "PATCH", "DELETE"])
class RealtyViewSet(viewsets.ModelViewSet):
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer

    @extend_schema(
        description='Создание недвижимости',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Недвижимость создана',
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
        description='Список всех существующих недвижимостей',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class(many=True)
            )
        },
    )
    def list(self, request, *args, **kwargs):
        data = json.loads(request.body)
        game_id = data.get('game_id')

        try:
            response = list_realtys(game_id)
            serialize = self.get_serializer(response).data
            return Response(serialize, status=status.HTTP_200_OK)
        except(Realty.DoesNotExist):
            return Response({'err':'Недвижимости не найдены'}, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        description='Получение сведений о недвижимости по ID',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description = 'Недвижимость не найдена'
            )
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description='Обновление недвижимости',
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
        description='Обновление части данных недвижимости',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление недвижимости',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Недвижимость удалена успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Недвижимость не найдена',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)