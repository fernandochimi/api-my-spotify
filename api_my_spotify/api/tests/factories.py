# coding: utf-8
import uuid
import factory

from datetime import datetime

from api.models import ApiToken, SpotifyInfo


class ApiTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApiToken

    token = uuid.uuid4()
    date_added = datetime.now()
    is_active = True


class SpotifyInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SpotifyInfo
