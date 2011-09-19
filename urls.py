from django.conf.urls.defaults import patterns, include, url
from tastypie.api import Api

from django.contrib import admin
from locations.api.resources import LocationResource
from comments.api.resources import CommentResource, UserResource

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(LocationResource())
v1_api.register(CommentResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'andromorb.views.home', name='home'),
    # url(r'^andromorb/', include('andromorb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^locations/', include('locations.urls')),
    url(r'^api/', include(v1_api.urls)),
)
