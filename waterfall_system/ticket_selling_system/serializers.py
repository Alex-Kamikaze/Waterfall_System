from .models import *
from rest_framework import serializers

class SessionInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionInfo
        fields = ["datetime_of_session", "places_left"]