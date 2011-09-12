from django.contrib.gis.geos.point import Point
from tastypie.constants import ALL
from tastypie.resources import ModelResource, Resource
from locations.models import Location

class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        allowed_methods = ['get']
        filtering = {
            'name':ALL,
        }

    def dehydrate(self, bundle):
        bundle.data['comments_count'] = bundle.obj.comments_count
        return bundle

    def apply_sorting(self, obj_list, options=None):
        if options:
            if "lat" in options and "lon" in options:
                point = Point(float(options["lat"]), float(options["lon"]))
                obj_list = obj_list.distance(point).order_by("distance")
                return obj_list
        return super(LocationResource, self).apply_sorting(obj_list, options)