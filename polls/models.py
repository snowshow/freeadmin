import datetime
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from django.utils.translation import ugettext_lazy as _
STATUS_CHOICES = [
    ('d', _('Draft')),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Choices(models.Model):
    stchois = models.CharField(max_length=200)
    def __unicode__(self):
        return "%s " % self.stchois
class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()
class TvRecord(models.Model):
    channel_id = models.Count
    channel_name = models.CharField(max_length=200)
    record_start = models.DateTimeField('record_start')
    record_end = models.DateTimeField('record_end')
    record_dur = models.IntegerField(_('record_dur'))
    reds = models.IntegerField('red')
    status = models.ForeignKey(Choices)
#    status = models.CharField(max_length=1, choices= STATUS_CHOICES)
    redsa = models.IntegerField('reda')
#    class MPTTMeta:
#       order_insertion_by = ['channel_name']
    def __unicode__(self):
        return "%s" % self.channel_name


class Genre(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return "%s genre" % self.name
#    class MPTTMeta:
 #       order_insertion_by = ['name']

class Modem(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.IntegerField()
    ip = models.IPAddressField(_('IP Address'))
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    mac = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s" % self.name
