from rest_framework import serializers
from .models import Opd


class OpdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opd
        fields = ['id', 'doctor', 'type', 'time', 'date', 'off', 'created_at', 'updated_at']
