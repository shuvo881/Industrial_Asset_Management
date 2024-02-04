from django import forms
from .models import Company, Employee, Device, DeviceTransection

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'

class DeviceTransectionForm(forms.ModelForm):
    class Meta:
        model = DeviceTransection
        fields = '__all__'
        #exclude = ['checkin_time']
