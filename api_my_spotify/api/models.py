# coding: utf-8
import uuid

from datetime import datetime

from django.db import models


class ApiToken(models.Model):
    token = models.UUIDField(
        u"token", default=uuid.uuid4, unique=True, primary_key=True)
    date_added = models.DateField(u"date added", default=datetime.now())
    is_active = models.BooleanField(u"active", default=True)

    class Meta:
        verbose_name, verbose_name_plural = u"API Token", u"API Tokens"

    def __unicode__(self):
        return u"{0}".format(self.token)


class SpotifyUser(models.Model):
    name = models.CharField(u"name", max_length=250)
    user_id = models.CharField(
        u"user id", max_length=128, primary_key=True, unique=True)
    followers = models.IntegerField(u"followers")
    picture = models.URLField(
        u"picture path", max_length=250, null=True, blank=True)
    link = models.URLField(u"url", max_length=250)

    class Meta:
        verbose_name, verbose_name_plural = u"Spotify User", u"Spotify Users"

    def __unicode__(self):
        return u"{0}".format(self.user_id)


class SpotifyUserPlaylist(models.Model):
    user = models.ForeignKey(SpotifyUser)
    name = models.CharField(u"name", max_length=250)
    link = models.URLField(u"url", max_length=250)
    playlist_id = models.CharField(
        u"playlist id", max_length=128, primary_key=True, unique=True)

    class Meta:
        verbose_name, verbose_name_plural = u"Spotify User Playlist",\
            u"Spotify Users Playlists"

    def __unicode__(self):
        return u"{0}".format(self.playlist_id)
