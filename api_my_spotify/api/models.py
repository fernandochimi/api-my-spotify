# coding: utf-8
import uuid

from datetime import datetime

from django.db import models


class ApiToken(models.Model):
    token = models.UUIDField(
        u'token', default=uuid.uuid4, unique=True, primary_key=True)
    date_added = models.DateField(u'date added', default=datetime.now())
    is_active = models.BooleanField(u'active', default=True)

    class Meta:
        verbose_name, verbose_name_plural = u"API Token", u"API Tokens"

    def __unicode__(self):
        return u"{0}".format(self.token)


class SpotifyInfo(models.Model):
    pass

    class Meta:
        verbose_name, verbose_name_plural = u"Spotify Info", u"Spotify Infos"
