from rest_framework import serializers

from .models import Player

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"