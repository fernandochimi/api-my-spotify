# coding: utf-8
from django.test import TestCase

from .factories import ApiTokenFactory, SpotifyUserFactory,\
    SpotifyUserPlaylistFactory


class ApiTokenTest(TestCase):
    def setUp(self):
        self.token = ApiTokenFactory()

    def test_01_unicode(self):
        "Token must be a unicode"
        self.assertEqual(unicode(self.token), u'{0}'.format(self.token.token))


class SpotifyUserTest(TestCase):
    def setUp(self):
        self.user = SpotifyUserFactory()

    def test_01_unicode(self):
        "User ID must be a unicode"
        self.assertEqual(unicode(self.user), u'{0}'.format(self.user.user_id))


class SpotifyUserPlaylistTest(TestCase):
    def setUp(self):
        self.playlist = SpotifyUserPlaylistFactory()

    def test_01_unicode(self):
        "Playlist ID must be a unicode"
        self.assertEqual(
            unicode(self.playlist), u'{0}'.format(self.playlist.playlist_id))
