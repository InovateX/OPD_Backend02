from urllib import response
from django.shortcuts import render
from rest_framework import viewsets
from .models import UserModel
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = UserModel.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def get_user_by_name(self, request, name=None):
        queryset = UserModel.objects.filter(name__icontains=name)
        serializer = self.get_serializer(queryset, many=True)
        return response(serializer.data)

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
