from rest_framework import viewsets, status
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse, OpenApiParameter, OpenApiExample

from ..serializers import GameSerializer
from ..models import Game

def examples(request_only = False):
    return [
        OpenApiExample(
            name='Successful response',
            value={
                'gametime': 30,
                'steptime': 15,
                'room': 1
            }
        )
    ]

def parameters(reqired = False):
    return [
        OpenApiParameter(
            name='steptime',
            description='Время хода (в секундах)',
            type=int,
            required=True
        ),
        OpenApiParameter(
            name='gametime',
            description='Время игры (в минутах)',
            type=int,
            required=True
        ),
        OpenApiParameter(
            name='room',
            description='Комната',
            type=int,
            required=True
        ),
    ]

@extend_schema(tags=['Game'])
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    @extend_schema(
        description='Получение сведений об игре по ID',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description = 'Игра не найдена'
            )
        },
        parameters=[
            OpenApiParameter(
                name='id',
                description='ID игры',
                type=int,
                required=False
            )
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        description='Список всех существующих игр',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class(many=True),
                examples=examples(True)
            )
        }
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, args, kwargs)

    @extend_schema(
        description='Создание игры',
        responses={
            status.HTTP_201_CREATED: OpenApiResponse(
                description='Игра создана',
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
        description='Обновление игры',
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
        description='Обновление части данных игры',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description='Данные обновлены'
            )
        }
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        description='Удаление игры',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Игра удалена успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Игра не найдена',
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    # @extend_schema(
    #     description='Создание игры через query',
    #     methods=['POST'],
    #     responses={
    #         status.HTTP_201_CREATED: OpenApiResponse(
    #             description='Игра создана',
    #             response=serializer_class
    #         ),
    #         status.HTTP_400_BAD_REQUEST: OpenApiResponse(
    #             description='Bad request'
    #         )
    #     },
    #     parameters=parameters(True)
    # )
    # def create(self, request, *args, **kwargs):
    #     query = request.query_params
    #     gametime = query.get('gametime')
    #     steptime = query.get('steptime')
    #     room = query.get('room')
    #     serializer = GameSerializer(
    #         data={
    #             'gametime': gametime,
    #             'steptime':steptime,
    #             'room':room
    #         }
    #     )
    #     serializer.is_valid(raise_exception=True)
    #     return super().create(serializer, *args, **kwargs)