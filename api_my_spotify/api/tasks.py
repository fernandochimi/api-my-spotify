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
    user, created = SpotifyUser.objects.get_or_create(
        name=user_id["name"],
        user_id=user_id["user_id"],
        followers=user_id["followers"],
        picture=user_id["picture"],
        link=user_id["link"],
    )
    logger.info(u"User {0} inserted with success".format(user.user_id))
    return user.user_id


@celery_app.task
def create_playlist(playlist):
    print playlist
    print dir(playlist)
    logger.info(
        u"Start creation of Playlist of the User {0}".format(
            playlist.get("name")))
    playlist, created = SpotifyUserPlaylist.objects.get_or_create(
        user=playlist.get("user_id"),
        name=playlist.get("name"),
        link=playlist.get("link"),
        playlist_id=playlist.get("playlist_id"),
    )
    logger.info(u"Playlist(s) inserted with success")
    return playlist.playlist_id
