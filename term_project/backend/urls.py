"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .api.views import index_view, MessageViewSet, CarViewSet, RepairViewSet, PersonViewSet, StantionViewSet, RepairWorkViewSet, ComponentViewSet, CarShopViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)
router.register('cars', CarViewSet)
router.register('repairs', RepairViewSet)
router.register('masters', PersonViewSet)
router.register('stantions', StantionViewSet)
router.register('works', RepairWorkViewSet)
router.register('components', ComponentViewSet)
router.register('shops', CarShopViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('', index_view, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/api/admin/
    path('api/admin/', admin.site.urls),
]


