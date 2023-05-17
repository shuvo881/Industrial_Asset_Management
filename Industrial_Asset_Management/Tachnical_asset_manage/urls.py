# Import necessary modules and functions
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmpoloyeeViewSet, DeviceViewSet

# Create a DefaultRouter instance
router = DefaultRouter()

# Register viewsets with corresponding URLs
router.register(r'companies/', CompanyViewSet)
router.register(r'employees/', EmpoloyeeViewSet)
router.register(r'devices/', DeviceViewSet)

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
]
