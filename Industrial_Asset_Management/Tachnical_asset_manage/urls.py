from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmpoloyeeViewSet, DeviceViewSet

router = DefaultRouter()
router.register(r'companies/', CompanyViewSet)
router.register(r'employees/', EmpoloyeeViewSet)
router.register(r'devices/', DeviceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]