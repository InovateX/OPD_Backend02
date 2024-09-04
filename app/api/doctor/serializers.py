from rest_framework import serializers
from .models import Doctor
from api.opd.serializers import OpdSerializer

class DoctorSerializer(serializers.ModelSerializer):
    opd = OpdSerializer()
    class Meta:
        model = Doctor
        fields = '__all__'
