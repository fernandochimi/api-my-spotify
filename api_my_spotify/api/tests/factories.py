# coding: utf-8
import uuid
import factory

from datetime import datetime

from api.models import ApiToken, SpotifyUser


class ApiTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ApiToken

    token = uuid.uuid4()
    date_added = datetime.now()
    is_active = True


class SpotifyUserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = SpotifyUser

    name = factory.Sequence(lambda n: "Fulano %s" % n)
    user_id = factory.Sequence(lambda n: "fulano%s" % n)
    followers = factory.Sequence(lambda n: "%d" % n)
    picture = factory.Sequence(
        lambda n: "https://fbcdn-profile-a.akamaihd.net/%s" % n)
    link = factory.Sequence(
        lambda n: "https://open.spotify.com/user/fulano%s" % n)
