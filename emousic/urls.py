from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'emousic'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name = 'index'),
    path('get_moodtags/', views.get_moodtags, name = 'get_moodtags'),
    #url(r'^get_moodtags/$', views.get_moodtags, name='get_moodtags'),
    # url(r'^get_moodtags/(?P<track_id>[0-9]+)/(?P<min>[0-9]+)/(?P<max>[0-9]+)/(?P<approach>[0-9]+)$',
    #     views.get_moodtags, name='get_moodtags'),
    path('rdf', views.rdf, name='rdf'),
    path('wildwebmidi.data', views.read_wildwebmidi, name='read_wildwebmidi')
]