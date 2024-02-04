from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee, Device, DeviceTransection
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceTransectionSerializer


# Viewset for the Company model
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# Viewset for the Employee model
class EmpoloyeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# Viewset for the Device model
class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class DeviceTransectionViewSet(viewsets.ModelViewSet):
    queryset = DeviceTransection.objects.all()
    serializer_class = DeviceTransectionSerializer