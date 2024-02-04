from django.db import models
from django.utils.translation import gettext as _



# Model for the Company entity
class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    

# Model for the Employee entity
class Employee(models.Model):
    SEX = {
        'male': 'male',
        'female': 'female',
        'others': 'others'
    }
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    present_address = models.CharField(max_length = 150)
    permanent_present_address = models.CharField(max_length = 150)
    age = models.IntegerField()
    sex = models.CharField(max_length = 150, choices=SEX)
    
    def __str__(self):
        return self.name
    
    
    

# Model for the Device entity
class Device(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    mac_address = models.CharField(_("MAC Address of Device"), max_length=50, unique=True)
    
    def __str__(self):
        return self.name


# Model of device transection

class DeviceTransection(models.Model):
    device_name = models.OneToOneField(Device, on_delete=models.CASCADE)
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    checkout_time = models.DateTimeField(auto_now_add=True)
    checkin_time = models.DateTimeField(null=True, blank=True)
    condition_on_checkout = models.TextField()
