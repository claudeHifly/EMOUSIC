from django.urls import path

from . import views

app_name = 'emousic'

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('get_moodtags/', views.get_moodtags, name='get_moodtags'),
    path('rdf', views.rdf, name='rdf'),
    path('wildwebmidi.data', views.read_wildwebmidi, name='read_wildwebmidi')
]
