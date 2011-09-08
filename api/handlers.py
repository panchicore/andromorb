from piston.handler import BaseHandler
from locations.models import Location
from comments.models import Comment
from django.contrib.gis.geos import Point

class LocationHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = Location
    fields = ('name','distance','id', 'address', 'longitude', 'latitude')

    def read(self, request, location_id=None):

        if location_id:
            return Location.objects.get(id=location_id)
        else:
            point = Point(float('4.6434186623500'), float('-74.0679576062'))
            return Location.objects.distance(point).order_by('distance')


class LocationCommentsHandler(BaseHandler):
    allowed_methods = ('GET','POST',)
    model = Comment
    fields = ('id', 'date', 'username', 'comment')

    """ api/location/comments/?lid=6 """
    def read(self, request):
        location_id = request.GET.get('lid')
        location = Location.objects.get(id=location_id)
        return location.comments.all().order_by('date')



