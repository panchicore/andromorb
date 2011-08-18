from django.contrib import admin
from locations.models import LocationType, Location

admin.site.register(Location)
admin.site.register(LocationType)
