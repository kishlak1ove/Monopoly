from rest_framework import viewsets, status
from drf_spectacular.views import extend_schema
from drf_spectacular.utils import OpenApiResponse
from rest_framework.response import Response
from rest_framework.decorators import action

from ..controllers.controller_invite import *
from ..serializers import InviteSerializer
from ..models import Invite, Room


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
        user = request.user
        room_id = request.query_params.get('room')

        try:
            room = Room.objects.get(id=room_id)
            response = create_invite(room, user)
            data = self.get_serializer(response).data
            return Response(data, status=status.HTTP_201_CREATED)
        except Room.DoesNotExist:
            return Response({'error': 'Комната не найдена'},status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=True)
    def accept(self, request, *args, **kwargs):
        invite_id = kwargs.get('pk')
        print(invite_id)
        try:
            invite = Invite.objects.get(id=invite_id)
            response, code = accept_invite(invite)
            return Response(response, status=code)
        except Invite.DoesNotExist:
            return Response({'error': 'Приглашение не найдено'}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=['GET'], detail=True)
    def denied(self, request, *args, **kwargs):
        invite_id = kwargs.get('pk')
        try:
            invite = Invite.objects.get(id=invite_id)
            response, code = denied_invite(invite)
            return Response(response, status=code)
        except Invite.DoesNotExist:
            return Response({'error': 'Приглашение не найдено'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Удаление приглашения',
        responses={
            status.HTTP_204_NO_CONTENT: OpenApiResponse(
                description='Приглашение удалено успешно',
            ),
            status.HTTP_404_NOT_FOUND: OpenApiResponse(
                description='Приглашение не найдено',
            )
        }
    )
    def destroy(self, request, *args, **kwargs):
        invite_id = kwargs.get('pk')
        try:
            invite = Invite.objects.get(id=invite_id)
            response, code = delete_invite(invite)
            return Response(response, status=code)
        except Invite.DoesNotExist:
            return Response({'error': 'Приглашение не найдено'}, status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        description='Список всех существующих приглашений',
        responses={
            status.HTTP_200_OK: OpenApiResponse(
                description = 'Successful response',
                response = serializer_class
            )
        }
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

