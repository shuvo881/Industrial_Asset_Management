# Import necessary modules and functions
from django.shortcuts import render
from rest_framework import viewsets
from .models import Company, Employee, Device
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer

# Create your views here.

# Viewset for the Company model
class CompanyViewSet(viewsets.ModelViewSet):
    # Retrieve all instances of the Company model
    queryset = Company.objects.all()
    # Use the CompanySerializer for serialization and deserialization
    serializer_class = CompanySerializer

# Viewset for the Employee model
class EmpoloyeeViewSet(viewsets.ModelViewSet):
    # Retrieve all instances of the Employee model
    queryset = Employee.objects.all()
    # Use the EmployeeSerializer for serialization and deserialization
    serializer_class = EmployeeSerializer

# Viewset for the Device model
class DeviceViewSet(viewsets.ModelViewSet):
    # Retrieve all instances of the Device model
    queryset = Device.objects.all()
    # Use the DeviceSerializer for serialization and deserialization
    serializer_class = DeviceSerializer
