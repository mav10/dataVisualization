from django.db import models
from django.utils import timezone
from rest_framework import serializers


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Organisation(models.Model):
    title =  models.CharField(max_length=15)
    address = models.CharField(max_length=20, blank=True, null=True)
    contacts = models.CharField(max_length=60, blank=True, null=True)

class Device(models.Model):
    title = models.CharField(max_length=15)
    model = models.CharField(max_length=5)
    serialNuber = models.CharField(max_length=10)

    country = models.CharField(max_length=20,
                               blank=True, null=True)

    def __str__(self):
        return self.title + self.serialNuber

class Patient(models.Model):
    GENDER_ENUM = (
        ('M', 'Man'),
        ('W', 'Woman'),
        ('N/A', 'nAn'),
    )
    name = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_ENUM)
    birthday_date = models.DateTimeField(
        default=timezone.now)
    lastVisit_date = models.DateTimeField(
        blank=True, null=True)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Statistics(models.Model):
    index_A = models.PositiveIntegerField()
    index_B = models.PositiveIntegerField()
    index_C = models.PositiveIntegerField()

    avg_index = models.PositiveIntegerField()

    def __str__(self):
        return ("A:{0} B:{1} C:{2} (avg:{3})".format(self.index_A, self.index_B, self.index_C, self.avg_index))

class TherapyDay(models.Model):
    therapy_date = models.DateTimeField(
        default=timezone.now)
    transmission_date = models.DateTimeField(
        default=timezone.now)
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    statistics = models.ForeignKey(Statistics, on_delete=models.CASCADE, null=True)

class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ('url', 'title', 'address', 'contacts', 'pk')

class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = ('url', 'title', 'model', 'serialNuber', 'country', 'pk')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    device = DeviceSerializer()
    organisation = OrganisationSerializer()

    class Meta:
        model = Patient
        fields = ('url', 'name', 'gender', 'birthday_date', 'lastVisit_date', 'device', 'organisation'
                                                                                        '', 'pk')

class StatisticsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Statistics
        fields = ('url', 'index_A', 'index_B', 'index_C', 'avg_index', 'pk')


class TherapyDaySerializer(serializers.HyperlinkedModelSerializer):
    device = DeviceSerializer()
    statistics = StatisticsSerializer()

    class Meta:
        model = TherapyDay
        fields = ('url', 'device', 'statistics', 'transmission_date', 'therapy_date', 'pk')

class ImportedFile(models.Model):
    value = models.CharField(max_length=128);
    description = models.CharField(max_length=256);
    def __str__(self):
        return self.value

class Date(models.Model):
    value = models.DateTimeField(unique=False)
    file = models.ForeignKey(ImportedFile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.value)

class Latitude(models.Model):
    value = models.FloatField(unique=False)
    def __str__(self):
        return str(self.value)

class Longitude(models.Model):
    value = models.FloatField(unique=False)
    bulk_ref=models.CharField(max_length=320)
    def __str__(self):
        return str(self.value)

class Temperature(models.Model):
    value = models.FloatField()
    latitude = models.ForeignKey(Latitude, on_delete=models.CASCADE, null=True)
    longitude = models.ForeignKey(Longitude, on_delete=models.CASCADE, null=True)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)
    importedFile = models.ForeignKey(ImportedFile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.value) + ', ' + str(self.date)

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImportedFile
        fields = ('url', 'value', 'description', 'pk')

class DateSerializer(serializers.HyperlinkedModelSerializer):
    file = FileSerializer()

    class Meta:
        model = Date
        fields = ('url', 'value', 'file', 'pk')

class LatitudeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Latitude
        fields = ('url', 'value', 'pk')

class LongitudeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Longitude
        fields = ('url', 'value', 'bulk_ref', 'pk')

class TemperatureSerializer(serializers.HyperlinkedModelSerializer):
    latitude = LatitudeSerializer()
    longitude = LongitudeSerializer()
    date = DateSerializer()
    importedFile = FileSerializer()

    class Meta:
        model = Temperature
        fields = ('url', 'value', 'date', 'latitude', 'longitude', 'importedFile', 'pk')