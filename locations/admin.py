from django.contrib import admin
from comments.models import Comment
from locations.models import LocationType, Location

class LocationCommentsStackedInline(admin.StackedInline):
    model = Comment
    extra = 1

class LocationAdmin(admin.ModelAdmin):
    inlines = [LocationCommentsStackedInline]
    list_display = ('name','comments_count')

admin.site.register(Location, LocationAdmin)
admin.site.register(LocationType)
