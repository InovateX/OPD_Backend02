from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import filters
from api.admission.models import Admission
from .serializers import AdmissionSerializer

class AdmissionPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'limit'  # Allow front-end to specify the page size
    max_page_size = 100  # Maximum limit

class AdmissionListView(ListAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer
    pagination_class = AdmissionPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['hospital']  # Filter by hospital or any other relevant field
    search_fields = ['name', 'mobile_no', 'address']  # Fields to search by

class AdmissionCreateView(CreateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class AdmissionDetailView(RetrieveAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class AdmissionUpdateView(UpdateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class AdmissionDeleteView(DestroyAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

# Create your views here.
