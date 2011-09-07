from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import LocationHandler

auth = HttpBasicAuthentication(realm='TestRealm')
ad = {'authentication' : auth}

location_handler = Resource(handler=LocationHandler, authentication=auth)

urlpatterns = patterns('',
    url(r'^locations/(?P<location_id>[\d+])/$', location_handler),
    url(r'^locations/$', location_handler),
)