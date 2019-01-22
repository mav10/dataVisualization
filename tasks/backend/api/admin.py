from django.contrib import admin

# Register your models here.
from .models import Patient, Device, TherapyDay, Statistics, Organisation, Temperature, Date, Longitude, Latitude

admin.site.register(Patient)
admin.site.register(Device)
admin.site.register(TherapyDay)
admin.site.register(Statistics)
admin.site.register(Organisation)

admin.site.register(Date)
admin.site.register(Latitude)
admin.site.register(Longitude)
admin.site.register(Temperature)