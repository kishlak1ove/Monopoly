from rest_framework import serializers

from .models import *

class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"

class RealtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Realty
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"