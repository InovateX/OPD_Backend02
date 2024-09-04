from django.urls import path
from .views import OPDDetailView, OPDByTypeView

urlpatterns = [
    path('api/opd/<int:pk>/', OPDDetailView.as_view(), name='opd_detail'),
    path('api/opd/type/<str:opd_type>/', OPDByTypeView.as_view(), name='opd_by_type'),
]
