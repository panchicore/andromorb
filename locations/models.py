from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

class LocationType(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Location(models.Model):
    type = models.ForeignKey(LocationType, null=True, blank=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(blank=True, null=True, verbose_name='Longitude')
    location = models.PointField(blank = True, null=True)
    
    objects = models.GeoManager()

    def save(self, *args, **kwargs):
        self.location = Point(self.latitude, self.longitude)
        super(Location, self).save(*args, **kwargs)


    def __unicode__(self):
        return self.name

from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django\.contrib\.gis\.db\.models\.fields\.PointField"])