from rest_framework import generics # type: ignore
from .models import Bed
from .serializers import BedSerializer

class BedByHospitalView(generics.ListAPIView):
    serializer_class = BedSerializer

    def get_queryset(self):
        hospital_id = self.kwargs['hospital_id']
        return Bed.objects.filter(hospital_id=hospital_id)

class BedByTypeView(generics.ListAPIView):
    serializer_class = BedSerializer

    def get_queryset(self):
        ward_type = self.kwargs['ward_type']
        return Bed.objects.filter(ward_type=ward_type)
