"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet,\
    PatientViewSet, DeviceViewSet, TherapyDayViewSet,\
    StatViewSet, OrganisationViewSet, DatesViewSet,\
    FilesViewSet, TemperatureViewSet, LongitudeViewSet, LatitudeViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('patients', PatientViewSet)
router.register('devices', DeviceViewSet)
router.register('statistics', StatViewSet)
router.register('therapy', TherapyDayViewSet)
router.register('organisations', OrganisationViewSet)
router.register('files', FilesViewSet)
router.register('dates', DatesViewSet)
router.register('temperature', TemperatureViewSet)
router.register('latitudes', LatitudeViewSet)
router.register('longitude', LongitudeViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),



    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),

]


