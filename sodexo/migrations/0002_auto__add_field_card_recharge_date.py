# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Card.recharge_date'
        db.add_column(u'sodexo_card', 'recharge_date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2014, 3, 19, 0, 0), auto_now=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Card.recharge_date'
        db.delete_column(u'sodexo_card', 'recharge_date')


    models = {
        u'sodexo.card': {
            'Meta': {'object_name': 'Card'},
            'balance': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recharge_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 19, 0, 0)', 'auto_now': 'True', 'blank': 'True'})
        },
        u'sodexo.meal': {
            'Meta': {'object_name': 'Meal'},
            'date': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'})
        },
        u'sodexo.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['sodexo']