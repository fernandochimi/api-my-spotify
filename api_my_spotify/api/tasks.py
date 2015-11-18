# coding: utf-8
import logging

from settings import celery_app

from models import SpotifyUser, SpotifyUserPlaylist

logger = logging.getLogger('api_my_spotify.api.tasks')


@celery_app.task
def create_user(user_id):
    logger.info(
        u"Start creation of User {0} with ID {1}".format(
            user_id["name"], user_id["user_id"]))
    pass
