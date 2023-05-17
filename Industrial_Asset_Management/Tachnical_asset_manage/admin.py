from django.contrib import admin
from .models import Company, Employee, Device

# Register your models here.

# Register the Company model with the admin site
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Register the Employee model with the admin site
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'company')
    list_filter = ('company',)

# Register the Device model with the admin site
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'assigned_to', 'assigned_date', 'returned_date', 'description',)
