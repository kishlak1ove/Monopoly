from rest_framework import serializers

from .models import Realty

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realty
        fields = "__all__"