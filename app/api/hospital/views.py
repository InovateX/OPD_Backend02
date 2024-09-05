# views.py
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from api.bed.models import Hospital
from .serializers import HospitalSerializer

# Custom pagination class
class HospitalPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Allow front-end to specify the page size
    max_page_size = 100  # Maximum limit

class HospitalListView(ListAPIView):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    pagination_class = HospitalPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['name', 'location']  # Fields to filter by
    search_fields = ['name', 'location']  # Fields to search by
