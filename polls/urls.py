from django.conf.urls.defaults import patterns, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:

#urlpatterns = patterns('polls.views',
#    url(r'^polls/$', 'index'),
#    url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),
#    url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),
#    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote')
#)
urlpatterns = patterns('polls.views',
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)

