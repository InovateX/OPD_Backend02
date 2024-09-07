from django.urls import path
from .views import OpdListView

urlpatterns = [
    path('', OpdListView.as_view(), name='opd-list'),
]

