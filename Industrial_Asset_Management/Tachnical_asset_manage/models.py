from django.db import models

# Create your models here.

# Model for the Company entity
class Company(models.Model):
    name = models.CharField(max_length=50)

# Model for the Employee entity
class Employee(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

# Model for the Device entity
class Device(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    assigned_to = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    assigned_date = models.DateTimeField(null=True, blank=True)
    returned_date = models.DateTimeField(null=True, blank=True)
    condition = models.CharField(max_length=255, blank=True)
