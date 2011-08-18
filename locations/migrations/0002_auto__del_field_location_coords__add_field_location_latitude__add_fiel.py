# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Location.coords'
        db.delete_column('locations_location', 'coords')

        # Adding field 'Location.latitude'
        db.add_column('locations_location', 'latitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Location.longitude'
        db.add_column('locations_location', 'longitude', self.gf('django.db.models.fields.FloatField')(null=True, blank=True), keep_default=False)

        # Adding field 'Location.location'
        db.add_column('locations_location', 'location', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Adding field 'Location.coords'
        db.add_column('locations_location', 'coords', self.gf('django.contrib.gis.db.models.fields.PointField')(default=1, blank=True), keep_default=False)

        # Deleting field 'Location.latitude'
        db.delete_column('locations_location', 'latitude')

        # Deleting field 'Location.longitude'
        db.delete_column('locations_location', 'longitude')

        # Deleting field 'Location.location'
        db.delete_column('locations_location', 'location')


    models = {
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'locations.locationtype': {
            'Meta': {'object_name': 'LocationType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['locations']
