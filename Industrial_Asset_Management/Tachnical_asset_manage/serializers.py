from rest_framework import serializers
from .models import Company, Employee, Device, DeviceTransection

# Serializer for the Company model
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Serializer for the Employee model
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Serializer for the Device model
class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceTransectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceTransection
        fields = '__all__'