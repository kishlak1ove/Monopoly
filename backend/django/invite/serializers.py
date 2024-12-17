from rest_framework import serializers

from .models import Invite

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = "__all__"