# coding: utf-8
import logging
import requests

from django.conf import settings
from django.conf.urls import patterns, url

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.exceptions import Unauthorized, HttpError
from restless.resources import skip_prepare

from models import ApiToken, SpotifyUser,\
    SpotifyUserPlaylist

logger = logging.getLogger("api_my_spotify.api.resources")


class BaseResource(DjangoResource):
    preparer = FieldsPreparer(fields={})

    def is_authenticated(self):
        try:
            self.token = ApiToken.objects.get(
                token=self.request.GET.get("token"), is_active=True)
            return True
        except ApiToken.DoesNotExist:
            raise Unauthorized


class SpotifyUserResource(BaseResource):
    fields = {
        "name": "name",
        "user_id": "user_id",
        "followers": "followers",
        "picture": "picture",
        "link": "link",
    }

    def __init__(self, *args, **kwargs):
        super(SpotifyUserResource, self).__init__(*args, **kwargs)
        self.http_methods.update({
            "user_playlist": {
                "GET": "user_playlist",
            },
        })

    def get_spotify_data(self, user_id):
        logger.info(u"Get User ID {0} from Spotify API".format(user_id))
        try:
            response = requests.get(
                settings.URL_API + user_id, timeout=5).json()
            print response
            return response
        except:
            logger.info(u"User with ID {0} does not exist".format(user_id))
            raise HttpError(msg=u"User with ID {0} not found".format(user_id))

    def queryset(self, request):
        return SpotifyUser.objects.all()

    def detail(self, pk):
        self.preparer.fields = self.fields
        print pk
        print type(pk)
        try:
            return self.queryset(request=self.request).get(user_id=pk)
        except:
            user_info = self.get_spotify_data(user_id=pk)
            return user_info

    @skip_prepare
    def user_playlist(self):
        playlist = SpotifyUserPlaylist.objects.all()
        return {
            "fields": {
                "user": playlist.user,
                "name": playlist.name,
                "link": playlist.link,
                "playlist_id": playlist.playlist_id,
            }
        }

    @classmethod
    def urls(cls, name_prefix=None):
        urlpatterns = super(SpotifyUserResource, cls).urls(
            name_prefix=name_prefix)
        return urlpatterns + patterns(
            "",
            url(r"^playlists/$", cls.as_view("user_playlist"),
                name=cls.build_url_name("user_playlist", name_prefix)),
        )
