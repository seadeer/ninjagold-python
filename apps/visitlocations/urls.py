from django.conf.urls import patterns, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^farm$', views.farm, name='farm'),
    url(r'^cave$', views.cave, name='cave'),
    url(r'^dojo$', views.dojo, name='dojo'),
    url(r'^dice$', views.dice, name='dice'),
    url(r'^restart$', views.restart, name='restart'),
]