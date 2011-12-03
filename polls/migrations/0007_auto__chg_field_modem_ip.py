# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Modem.ip'
        db.alter_column('polls_modem', 'ip', self.gf('django.db.models.fields.CharField')(max_length=10))


    def backwards(self, orm):
        
        # Changing field 'Modem.ip'
        db.alter_column('polls_modem', 'ip', self.gf('django.db.models.fields.IPAddressField')(max_length=15))


    models = {
        'polls.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polls.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {})
        },
        'polls.choices': {
            'Meta': {'object_name': 'Choices'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stchois': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'polls.genre': {
            'Meta': {'object_name': 'Genre'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['polls.Genre']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'polls.modem': {
            'Meta': {'object_name': 'Modem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'phone_number': ('django.db.models.fields.IntegerField', [], {})
        },
        'polls.poll': {
            'Meta': {'object_name': 'Poll'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'polls.tvrecord': {
            'Meta': {'object_name': 'TvRecord'},
            'channel_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'record_dur': ('django.db.models.fields.IntegerField', [], {}),
            'record_end': ('django.db.models.fields.DateTimeField', [], {}),
            'record_start': ('django.db.models.fields.DateTimeField', [], {}),
            'reds': ('django.db.models.fields.IntegerField', [], {}),
            'redsa': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['polls.Choices']"})
        }
    }

    complete_apps = ['polls']
