from django.urls import path
from .views import HospitalDetailView, HospitalQueryView

urlpatterns = [
    path('hospitals/<int:pk>/', HospitalDetailView.as_view(), name='hospital-detail'),
    path('hospitals/', HospitalQueryView.as_view(), name='hospital-query'),
]
