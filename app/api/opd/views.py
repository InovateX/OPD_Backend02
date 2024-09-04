from django.shortcuts import render

from rest_framework import generics
from .models import Opd
from .serializers import OpdSerializer


class OPDDetailView(generics.RetrieveAPIView):
    queryset = Opd.objects.all()
    serializer_class = OpdSerializer

class OPDByTypeView(generics.ListAPIView):
    serializer_class = OpdSerializer

    def get_queryset(self):
        opd_type = self.kwargs['opd_type']
        return Opd.objects.filter(type=opd_type)

# Create your views here.
