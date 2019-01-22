from django.db import models
from django.db import transaction
from netCDF4 import num2date, Dataset as NetCDFFile
import numpy as np
from ..models import Temperature, Longitude, Latitude, Date, ImportedFile

class netcdfObject:


    def readFile(self):
        nc_file = 'C:/Users/Maxim/Downloads/_grib2netcdf-atls12-a82bacafb5c306db76464bc7e824bb75-RIwsLe.nc'
        nc = NetCDFFile(nc_file, mode='r')

        lat = nc.variables['latitude'][:]
        lon = nc.variables['longitude'][:]
        time = nc.variables['time'][:]
        t2 = nc.variables['t2m'][:]  # 2 meter temperature

        dates = num2date(nc.variables['time'][:],units=nc.variables['time'].units,calendar=nc.variables['time'].calendar)
        importedFile = ImportedFile(value=nc_file, description=str(t2.shape))
        importedFile.save()
        for t in range(len(dates)):
            date = Date(value = dates[t], file=importedFile)
            date.save()
            print('---------------------------------')
            for la in range(len(lat)):
                latitude = Latitude(value = lat[la])
                latitude.save()
                temps = [];
                lons= [];

                bulk_ref=nc_file + str(t) + str(la);
                for lo in range(len(lon)):
                    longitude = Longitude(value=lon[lo], bulk_ref=bulk_ref)
                    lons.append(longitude)

                Longitude.objects.bulk_create(lons)
                new_lons = Longitude.objects.filter(bulk_ref=bulk_ref)
                for slo in range(len(new_lons)):
                    temp = Temperature(value=t2[t][la][lo])
                    temp.date = date
                    temp.latitude = latitude
                    temp.importedFile = importedFile
                    temp.longitude = new_lons[slo]

                    temps.append(temp)

                Temperature.objects.bulk_create(temps)
                print(t, la, 'save temps set')

        nc.close()