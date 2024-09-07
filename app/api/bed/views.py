from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters
from api.bed.models import Bed
from .serializers import BedSerializer

class BedPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Allow front-end to specify the page size
    max_page_size = 100  # Maximum limit

class BedListView(ListAPIView):
    queryset = Bed.objects.all()
    serializer_class = BedSerializer
    pagination_class = BedPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['ward_type']
    search_fields = ['ward_type']  # Fields to filter by