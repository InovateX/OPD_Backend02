from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from api.opd.models import Opd
from .serializers import OpdSerializer

# Custom pagination class
class OpdPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Allow front-end to specify the page size
    max_page_size = 100  # Maximum limit

class OpdListView(ListAPIView):
    queryset = Opd.objects.all()
    serializer_class = OpdSerializer
    pagination_class = OpdPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['type' , 'date']  # Fields to filter by
    search_fields = ['type' , 'date']  # Fields to search by
