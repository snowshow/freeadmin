# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Choices'
        db.create_table('polls_choices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stchois', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('polls', ['Choices'])


    def backwards(self, orm):
        
        # Deleting model 'Choices'
        db.delete_table('polls_choices')


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
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        }
    }

    complete_apps = ['polls']
