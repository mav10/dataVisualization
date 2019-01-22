from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from rest_framework import viewsets
from .netcdf.index import netcdfObject

from .models import \
    Message, MessageSerializer,\
    Patient, PatientSerializer,\
    Device, DeviceSerializer,\
    Statistics, StatisticsSerializer,\
    TherapyDay, TherapyDaySerializer,\
    Organisation, OrganisationSerializer,\
    Date, DateSerializer,\
    Temperature, TemperatureSerializer,\
    Longitude, LongitudeSerializer,\
    LatitudeSerializer, Latitude,\
    ImportedFile, FileSerializer


# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows messages to be viewed or edited.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class PatientViewSet(viewsets.ModelViewSet):
    """
    API for patient with included entites like a device, therapy days and statistics
    """
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get_queryset(self):
        """
        by filtering against a `orgId` query parameter in the URL.
        """
        queryset = Patient.objects.all()
        orgId = self.request.GET.get('organisation', None)
        if orgId is not None:
            queryset = queryset.filter(organisation__pk=orgId)
        return queryset


class DeviceViewSet(viewsets.ModelViewSet):
    """
    API for patient with included entites like a device, therapy days and statistics
    """
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class StatViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class TherapyDayViewSet(viewsets.ModelViewSet):
    queryset = TherapyDay.objects.all()
    serializer_class = TherapyDaySerializer

    def get_queryset(self):
        """
        by filtering against a `deviceId` query parameter in the URL.
        """
        queryset = TherapyDay.objects.all()
        devId = self.request.GET.get('device', None)
        if devId is not None:
            queryset = queryset.filter(device__pk=devId)
        return queryset

class OrganisationViewSet(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

class FilesViewSet(viewsets.ModelViewSet):
    queryset = ImportedFile.objects.all()
    serializer_class = FileSerializer

class LongitudeViewSet(viewsets.ModelViewSet):
    queryset = Longitude.objects.all()
    serializer_class = LongitudeSerializer

class LatitudeViewSet(viewsets.ModelViewSet):
    queryset = Latitude.objects.all()
    serializer_class = LatitudeSerializer

class DatesViewSet(viewsets.ModelViewSet):
    queryset = Date.objects.all()
    serializer_class = DateSerializer

    def get_queryset(self):
        """
        by filtering against a `deviceId` query parameter in the URL.
        """
        queryset = Date.objects.all()
        fileId = self.request.GET.get('file', None)
        if fileId is not None:
            queryset = queryset.filter(file__pk=fileId)
        return queryset

class TemperatureViewSet(viewsets.ModelViewSet):
    """
    API for patient with included entites like a device, therapy days and statistics
    """
    queryset = Temperature.objects.all()
    serializer_class = TemperatureSerializer

    def get_queryset(self):
        """
        by filtering against a `date` query parameter in the URL.
        """
        queryset = ""
        dateId = self.request.GET.get('date', None)
        print('-----------${dateId}---------', dateId)
        if dateId is not None:
            queryset = Temperature.objects.select_related('date', 'longitude', 'latitude', 'importedFile').filter(date__pk=dateId)[0:1000]
        return queryset

class ImportFile(viewsets.ModelViewSet):
    newFile = netcdfObject()
    #newFile.readFile()

    interact(draw, timeItem=(0, len(time) - 1, 1))

