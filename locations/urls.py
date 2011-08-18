from django.conf.urls.defaults import *

urlpatterns = patterns('locations.views',
    url('^nearest_to_point/$', 'get_nearest_to_point', name='get_nearest_to_point'),
)