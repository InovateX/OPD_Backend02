from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Hospital
from .serializers import HospitalSerializer
from django.shortcuts import get_object_or_404

class HospitalDetailView(generics.RetrieveAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    
    def get(self, request, *args, **kwargs):
        hospital_id = kwargs.get('pk')
        hospital = get_object_or_404(Hospital, id=hospital_id)
        serializer = self.get_serializer(hospital)
        return Response(serializer.data)

class HospitalQueryView(generics.ListAPIView):
    serializer_class = HospitalSerializer

    def get_queryset(self):
        queryset = Hospital.objects.all()
        name = self.request.query_params.get('name', None)
        location = self.request.query_params.get('location', None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset
