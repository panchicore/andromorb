from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from api.handlers import LocationHandler, LocationCommentsHandler

auth = HttpBasicAuthentication(realm='TestRealm')
ad = {'authentication' : auth}

#location_handler = Resource(handler=LocationHandler, authentication=auth)
location_handler = Resource(handler=LocationHandler)
location_comments_handler = Resource(handler=LocationCommentsHandler)

urlpatterns = patterns('',
    url(r'^locations/(?P<location_id>[\d+])/$', location_handler),
    url(r'^locations/$', location_handler),
    url(r'^location/comments/$', location_comments_handler),
)