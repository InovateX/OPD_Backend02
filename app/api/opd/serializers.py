from rest_framework import serializers
from .models import Opd


class OpdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opd
        fields = '__all__'
