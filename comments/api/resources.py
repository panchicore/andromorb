from django.template.defaultfilters import timesince
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from comments.models import Comment
from django.contrib.auth.models import User
from locations.api.resources import LocationResource

class UserResource(ModelResource):
    class Meta:
        resource_name = 'user'
        queryset = User.objects.all()
        excludes = ['email', 'password', 'is_active', 'is_staff', 'is_superuser']


class CommentResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    #location = fields.ForeignKey(LocationResource, 'location', full=True)
    class Meta:
        queryset = Comment.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        full = True
        authorization = Authorization()

    def apply_sorting(self, obj_list, options=None):
        if options:
            if "loc_id" in options:
                obj_list = obj_list.filter(location__id=options["loc_id"])
                return obj_list
        return super(CommentResource, self).apply_sorting(obj_list, options)

    def dehydrate(self, bundle):
        comment = bundle.obj
        bundle.data["date_since"] = timesince(comment.date)
        return bundle
  