from piston.handler import BaseHandler
from locations.models import Location
from django.contrib.gis.geos import Point

class LocationHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Location
    fields = ('name','distance','id', ('type',('name',)))

    def read(self, request, location_id=None):

        if location_id:
            return Location.objects.get(id=location_id)
        else:
            point = Point(float('4.6434186623500'), float('-74.0679576062'))
            return Location.objects.distance(point).order_by('distance')