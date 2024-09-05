# serializers.py
from rest_framework import serializers
from api.bed.models import Hospital
class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'
