from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet
from . import views

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')

urlpatterns = [
    path('', include(router.urls)),
    #path('', views.SomeView.as_view(), name='some-view'),
]
