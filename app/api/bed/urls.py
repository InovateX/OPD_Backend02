from django.urls import path
from .views import BedListView
urlpatterns = [
    path('', BedListView.as_view(), name='bed-list'),
]