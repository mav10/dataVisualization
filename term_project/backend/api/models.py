
from django.db import models
from rest_framework import serializers
from django.utils import timezone


class Message(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'subject', 'body', 'pk')


class Car(models.Model):
    name = models.CharField(max_length=30)
    milage = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=30)
    isMaster = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CarShop(models.Model):
    titile = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.titile + ', ' + self.address


class RepairStation(models.Model):
    titile = models.CharField(max_length=100)
    address = models.CharField(max_length=256)
    latitude = models.FloatField()
    longitude = models.FloatField()
    isStation = models.BooleanField(default=True)

    def __str__(self):
        return self.titile + ', ' + self.address

class Reapir(models.Model):
    date = models.DateTimeField(default=timezone.now)
    milage = models.PositiveIntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=False)
    place = models.ForeignKey(RepairStation, on_delete=models.CASCADE, null=False)
    master = models.ForeignKey(Person, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.place) + ' at:' + str(self.date)

class Component(models.Model):
    repair = models.ForeignKey(Reapir, on_delete=models.CASCADE, null=True)
    titile = models.CharField(max_length=100)
    price = models.FloatField()
    country = models.CharField(max_length=12)
    purchase_place = models.ForeignKey(CarShop, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.titile

class RepairWork(models.Model):
    WORK_ENUM = (
        ('E', 'Engine'),
        ('T', 'Transmission'),
        ('U', 'ECU'),
        ('B', 'Body'),
        ('I', 'Interior'),
        ('O', 'Other'),
        ('S', 'Suspension'),
    )
    repair = models.ForeignKey(Reapir, on_delete=models.CASCADE, null=True)
    titile = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=1, choices=WORK_ENUM)

    def __str__(self):
        return self.category + ': ' + self.titile

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('url', 'name', 'milage', 'pk')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('url', 'name', 'isMaster', 'pk')

class StantionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairStation
        fields = ('url', 'titile', 'address', 'latitude', 'longitude', 'isStation', 'pk')

class RepairSerializer(serializers.HyperlinkedModelSerializer):
    car = CarSerializer()
    place = StantionSerializer()
    master = PersonSerializer()

    class Meta:
        model = Reapir
        fields = ('url', 'date', 'milage', 'car', 'place', 'master', 'pk')

class RepairWorkSerializer(serializers.HyperlinkedModelSerializer):
    repair = RepairSerializer()

    class Meta:
        model = RepairWork
        fields = ('url', 'repair', 'titile', 'price', 'category', 'pk')

class CarShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarShop
        fields = ('url', 'titile', 'address', 'latitude', 'longitude', 'pk')

class ComponentsSerializer(serializers.HyperlinkedModelSerializer):
    repair = RepairSerializer()
    purchase_place = CarShopSerializer()

    class Meta:
        model = Component
        fields = ('url', 'repair', 'titile', 'price', 'country', 'purchase_place', 'pk')