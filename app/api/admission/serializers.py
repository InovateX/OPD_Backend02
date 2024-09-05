# # serializers.py
from rest_framework import serializers
from api.hospital.models import Hospital
from api.admission.models import Admission

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = '__all__'
    
    def get_hospital_serializer(self):
        from api.hospital.serializers import HospitalSerializer
        return HospitalSerializer
