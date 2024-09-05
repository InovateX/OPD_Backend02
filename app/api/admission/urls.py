from django.urls import path
from .views import AdmissionListView, AdmissionCreateView, AdmissionDetailView, AdmissionUpdateView, AdmissionDeleteView

urlpatterns = [
    path('admissions/', AdmissionListView.as_view(), name='admission-list'),
    path('admissions/create/', AdmissionCreateView.as_view(), name='admission-create'),
    path('admissions/<int:pk>/', AdmissionDetailView.as_view(), name='admission-detail'),
    path('admissions/<int:pk>/update/', AdmissionUpdateView.as_view(), name='admission-update'),
    path('admissions/<int:pk>/delete/', AdmissionDeleteView.as_view(), name='admission-delete'),
]
