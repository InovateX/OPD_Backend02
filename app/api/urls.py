from django.contrib import admin
from django.urls import path, include

urlpatterns =[
    # path('beds/', include('api.bed.urls')),
    # path('doctors/', include('api.doctor.urls')),
    path('hospitals/', include('api.hospital.urls')),
    # path('opds/', include('api.opd.urls')),  # Ensure 'bed.urls' is correct
]


