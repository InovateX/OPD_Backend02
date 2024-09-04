from django.urls import path
from .views import BedByHospitalView, BedByTypeView

urlpatterns = [
    path('hospital/<int:hospital_id>/', BedByHospitalView.as_view(), name='beds-by-hospital'),
    # path('beds/type/<str:ward_type>/', BedByTypeView.as_view(), name='beds-by-type'),
]
