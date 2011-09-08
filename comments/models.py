from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from locations.models import Location

class Comment(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location, related_name='comments')
    comment = models.TextField(null=False, blank=False)
    date = CreationDateTimeField()

    def __unicode__(self):
        return '%s comments on %s: %s' % (self.user.username, self.location.name, self.comment)

    @property
    def username(self):
        return self.user.username
