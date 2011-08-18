# Create your views here
from django.http import HttpResponse
from django.utils import simplejson
from django.contrib.gis.geos import Point

#http://localhost:8000/locations/nearest_to_point/?lat=4.679467&long=-74.050083
from locations.models import Location

def get_nearest_to_point(request):
    latitude = request.GET.get('lat', 0)
    longitude = request.GET.get('long', 0)

    point = Point(float(latitude), float(longitude))
    locations = Location.objects.distance(point).order_by('distance')

    list = []
    for location in locations:
        list.append({'name':location.name,
                     'distance':location.distance.m,
                     'latitude':location.location.x,
                     'longitude':location.location.y,
                     'address':location.address,
                     'id':location.id,
                     'type':{
                            'id':location.type.id,
                            'name':location.type.name
                            }
                    })

    return HttpResponse(simplejson.dumps(list), mimetype='application/json')
