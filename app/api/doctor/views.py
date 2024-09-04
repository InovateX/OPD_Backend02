from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .models import Doctor
from .serializers import DoctorSerializer


class DoctorViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Doctor.objects.all()
            serializer = DoctorSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_doctor_by_name(self, request):
        try:
            name = request.GET.get('name')
            if not name:
                return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                doctor = Doctor.objects.get(name=name)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Doctor.DoesNotExist:
                return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_doctor_by_opd(self, request):
        try:
            opd = request.GET.get('opd')
            if not opd:
                return Response({"error": "OPD parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                doctor = Doctor.objects.filter(opd=opd).first()
                if doctor:
                    serializer = DoctorSerializer(doctor)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "No doctor found with the given OPD"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DoctorViewSet(viewsets.ViewSet):
    def list(self, request):
        try:
            queryset = Doctor.objects.all()
            serializer = DoctorSerializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_doctor_by_name(self, request):
        try:
            name = request.GET.get('name')
            if not name:
                return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                doctor = Doctor.objects.get(name=name)
                serializer = DoctorSerializer(doctor)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Doctor.DoesNotExist:
                return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_doctor_by_opd(self, request):
        try:
            opd = request.GET.get('opd')
            if not opd:
                return Response({"error": "OPD parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                doctor = Doctor.objects.filter(opd=opd).first()
                if doctor:
                    serializer = DoctorSerializer(doctor)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"error": "No doctor found with the given OPD"}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
