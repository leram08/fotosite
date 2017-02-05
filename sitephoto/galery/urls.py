from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from .models import Item, Photo


urlpatterns = patterns('',
  url(r'^$', ListView.as_view(
    model=Item,
    context_object_name='albums',
    template_name='album.html'),
    name='gallery'
    ),
  url(r'^(?P<slug>[\w-]+)/$', DetailView.as_view(
    model=Item,
    context_object_name='photos',
    template_name='photo.html'),
    name='photos'

    ),
)
