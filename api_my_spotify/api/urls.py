# coding: utf-8
from django.conf.urls import patterns, url

from api.resources import SpotifyUserResource


urlpatterns = patterns(
    "",
    url(
        r'api/v1/suser/(?P<pk>[-\w]+)/$',
        SpotifyUserResource.as_detail(), name="api_suser_detail"),
)
