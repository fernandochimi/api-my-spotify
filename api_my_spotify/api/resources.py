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
from tasks import create_user

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

    def get_user_data(self, user_id):
        logger.info(u"Get User ID {0} from Spotify API".format(user_id))
        try:
            response = requests.get(
                settings.URL_API + user_id, timeout=5).json()
            return self.prepare_user_data(response)
        except:
            logger.info(u"User with ID {0} does not exist".format(user_id))
            raise HttpError(msg=u"User with ID {0} not found".format(user_id))

    def prepare_user_data(self, user_id):
        try:
            picture_user = user_id["images"][0].get("url")
        except:
            picture_user = None
        return {
            "name": user_id.get("display_name"),
            "user_id": user_id.get("id"),
            "followers": user_id.get("followers").get("total"),
            "picture": picture_user,
            "link": user_id.get("external_urls").get("spotify"),
        }

    def get_playlist_data(self, playlist):
        logger.info(
            u"Get Playlist of User {0} from Spotify API".format(
                playlist.user.name))
        try:
            response = requests.get(
                settings.URL_API +
                playlist.user.user_id + "/playlist/", timeout=5).json()
            return self.prepare_playlist_data(response)
        except:
            logger.info(
                u"Playlist of User {0} does not exist".format(
                    playlist.user.name))
            raise HttpError(
                msg=u"Playlist of User {0} not found".format(
                    playlist.user.name))

    def queryset(self, request):
        return SpotifyUser.objects.all()

    def detail(self, pk):
        self.preparer.fields = self.fields
        try:
            return self.queryset(request=self.request).get(user_id=pk)
        except:
            user_info = self.get_user_data(user_id=pk)
            user_task = create_user.delay(user_info)
            return self.queryset(request=self.request).get(
                user_id=user_task.get("user.user_id"))

    @skip_prepare
    def user_playlist(self):
        print self
        print dir(self)
        self.preparer.fields = self.fields
        try:
            playlist = SpotifyUserPlaylist.objects.all()
        except:
            # get_playlist = self.get_playlist_data(self.)
            pass
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
