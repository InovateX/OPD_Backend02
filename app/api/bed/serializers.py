from rest_framework import serializers
from .models import Bed
from api.hospital.serializers import HospitalSerializer

class BedSerializer(serializers.ModelSerializer):
    hospital = HospitalSerializer()

    class Meta:
        model = Bed
        fields = '__all__'
