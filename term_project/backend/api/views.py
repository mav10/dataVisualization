from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets

from .models import Message, MessageSerializer, \
    Car, CarSerializer, \
    Person, PersonSerializer, \
    RepairStation, StantionSerializer,\
    Reapir, RepairSerializer,\
    CarShop, CarShopSerializer,\
    RepairWork, RepairWorkSerializer,\
    Component, ComponentsSerializer

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class CarViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class PersonViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class StantionViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = RepairStation.objects.all()
    serializer_class = StantionSerializer

class CarShopViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = CarShop.objects.all()
    serializer_class = CarShopSerializer

class ComponentViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = Component.objects.all()
    serializer_class = ComponentsSerializer
    def get_queryset(self):
        """
        by filtering `car` query parameter in the URL.
        """
        queryset = ""
        repairId = self.request.GET.get('repair', None)
        if repairId is not None:
            queryset = Component.objects.select_related('repair').filter(
                repair__pk=repairId)
        carId = self.request.GET.get('car', None)
        if carId is not None:
            queryset = Component.objects.select_related('repair').filter(
                repair__car__pk=carId)
        return queryset
	
	

class RepairWorkViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = RepairWork.objects.all()
    serializer_class = RepairWorkSerializer
	
    def get_queryset(self):
        """
        by filtering `car` query parameter in the URL.
        """
        queryset = ""
        repairId = self.request.GET.get('repair', None)
        carId = self.request.GET.get('car', None)
		
        if repairId is not None:
            queryset = RepairWork.objects.select_related('repair').filter(repair__pk=repairId)

        if carId is not None:
            queryset = RepairWork.objects.select_related('repair').filter(
					repair__car__pk=carId)

        return queryset

class RepairViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows cars to be viewed or edited.
        """
    queryset = Reapir.objects.all()
    serializer_class = RepairSerializer

    def get_queryset(self):
        """
        by filtering `car` query parameter in the URL.
        """
        queryset = ""
        carId = self.request.GET.get('car', None)
        if carId is not None:
            queryset = Reapir.objects.select_related('master', 'car', 'place').filter(
                car__pk=carId)
        repairId = self.request.GET.get('id', None)
        if repairId is not None:
            queryset = Reapir.objects.select_related('master', 'car', 'place').filter(
                pk=repairId)
        return queryset
