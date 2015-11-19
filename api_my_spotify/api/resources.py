# coding: utf-8
import logging
import requests

from django.conf import settings

from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer
from restless.exceptions import Unauthorized, HttpError

from models import ApiToken, SpotifyUser
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


class SpotifyResource(BaseResource):
    fields = {
        "name": "name",
        "user_id": "user_id",
        "followers": "followers",
        "picture": "picture",
        "link": "link",
    }

    def get_user_data(self, user_id):
        logger.info(u"Get User ID {0} from Spotify API".format(user_id))
        try:
            response = requests.get(
                settings.URL_API + user_id, timeout=5).json()
            logger.debug(
                u"Get User ID {0} to prepare with success".format(user_id))
            return self.prepare_user_data(response)
        except:
            logger.error(u"User with ID {0} does not exist".format(user_id))
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
