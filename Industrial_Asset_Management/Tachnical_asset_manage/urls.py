# Import necessary modules and functions
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CompanyViewSet, EmpoloyeeViewSet, DeviceViewSet, DeviceTransectionViewSet
from .views import (
        CompanyListView, 
        CompanyCreateView,
        CompanyUpdateView,
        CompanyDeleteView,
        CompanyDetailView,
        
        EmployeeListView, 
        EmployeeCreateView,
        EmployeeUpdateView,
        EmployeeDeleteView,
        EmployeeDetailView,
        
        DeviceListView, 
        DeviceCreateView,
        DeviceUpdateView,
        DeviceDeleteView,
        DeviceDetailView,
        
        DeviceTransectionListView, 
        DeviceTransectionCreateView,
        DeviceTransectionUpdateView,
        DeviceTransectionDeleteView,
        DeviceTransectionDetailView,
        
        Home
    )

#from .views import CompanyListView

# Create a DefaultRouter instance
router = DefaultRouter()

# Register viewsets with corresponding URLs
router.register('companies', CompanyViewSet, basename='company')
router.register('employees', EmpoloyeeViewSet, basename='employee')
router.register('devices', DeviceViewSet, basename='devices')
router.register('devices-transction', DeviceTransectionViewSet, basename='devices-transction')

# Define the URL patterns
urlpatterns = [
    path('',Home.as_view(), name='home'),
    
    # api url
    path('api/', include(router.urls), name='apis'),
    
    # for company urls
    path('companies/', CompanyListView.as_view(), name='company_list'),
    path('companies/create/', CompanyCreateView.as_view(), name='company_create'),
    path('companies/edit/<int:pk>/', CompanyUpdateView.as_view(), name='company_update'),
    path('companies/delete/<int:pk>/', CompanyDeleteView.as_view(), name='company_delete'),
    path('companies/details/<int:pk>/', CompanyDetailView.as_view(), name='company_details'),
    
    # Employee urls
    
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/edit/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('employees/details/<int:pk>/', EmployeeDetailView.as_view(), name='employee_details'),
    
    # Device urls
    
    path('devices/', DeviceListView.as_view(), name='device_list'),
    path('devices/create/', DeviceCreateView.as_view(), name='device_create'),
    path('devices/edit/<int:pk>/', DeviceUpdateView.as_view(), name='device_update'),
    path('devices/delete/<int:pk>/', DeviceDeleteView.as_view(), name='device_delete'),
    path('devices/details/<int:pk>/', DeviceDetailView.as_view(), name='device_details'),
    
    # DeviceTransection urls
    
    path('devices_trans/', DeviceTransectionListView.as_view(), name='device_trans_list'),
    path('devices_trans/create/', DeviceTransectionCreateView.as_view(), name='device_trans_create'),
    path('devices_trans/edit/<int:pk>/', DeviceTransectionUpdateView.as_view(), name='device_trans_update'),
    path('devices_trans/delete/<int:pk>/', DeviceTransectionDeleteView.as_view(), name='device_trans_delete'),
    path('devices_trans/details/<int:pk>/', DeviceTransectionDetailView.as_view(), name='device_trans_details'),
]