# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'stdpage'
        db.create_table(u'stdpage_stdpage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('regno', self.gf('django.db.models.fields.IntegerField')(max_length=8)),
            ('fname', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('lname', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('sex', self.gf('django.db.models.fields.BooleanField')()),
            ('year', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'stdpage', ['stdpage'])

        # Adding model 'upoad1'
        db.create_table(u'stdpage_upoad1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('thumbnail', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'stdpage', ['upoad1'])

        # Adding model 'status1'
        db.create_table(u'stdpage_status1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stats', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('syear', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user1', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'stdpage', ['status1'])

        # Adding model 'comment'
        db.create_table(u'stdpage_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user_1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('comments', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('Status1', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stdpage.status1'])),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'stdpage', ['comment'])


    def backwards(self, orm):
        # Deleting model 'stdpage'
        db.delete_table(u'stdpage_stdpage')

        # Deleting model 'upoad1'
        db.delete_table(u'stdpage_upoad1')

        # Deleting model 'status1'
        db.delete_table(u'stdpage_status1')

        # Deleting model 'comment'
        db.delete_table(u'stdpage_comment')


    models = {
        u'stdpage.comment': {
            'Meta': {'object_name': 'comment'},
            'Status1': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stdpage.status1']"}),
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user_1': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stdpage.status1': {
            'Meta': {'object_name': 'status1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stats': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'syear': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'user1': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'stdpage.stdpage': {
            'Meta': {'object_name': 'stdpage'},
            'fname': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lname': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'regno': ('django.db.models.fields.IntegerField', [], {'max_length': '8'}),
            'sex': ('django.db.models.fields.BooleanField', [], {}),
            'year': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'stdpage.upoad1': {
            'Meta': {'object_name': 'upoad1'},
            'flname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumbnail': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['stdpage']