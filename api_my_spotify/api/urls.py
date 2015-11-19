# coding: utf-8
from django.conf.urls import patterns, url

from api.resources import SpotifyResource


urlpatterns = patterns(
    "",
    url(
        r'api/v1/suser/(?P<pk>[-\w]+)/$',
        SpotifyResource.as_detail(), name="api_suser_detail"),
)
