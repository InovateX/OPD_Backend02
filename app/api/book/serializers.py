from rest_framework import serializers
from .models import Book
from api.doctor.serializers import DoctorSerializer

class BookSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
