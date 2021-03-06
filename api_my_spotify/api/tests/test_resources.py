# coding: utf-8
from django.test import TestCase

from api.tasks import create_user

from factories import ApiTokenFactory, SpotifyUserFactory


class SpotifyResourceTest(TestCase):
    def setUp(self):
        self.token = ApiTokenFactory()
        self.user = SpotifyUserFactory()

        self.new_user = SpotifyUserFactory.create(
            name="De Tal Fulano",
            user_id="detalfulano",
            followers="4",
            picture=None,
            link="https://open.spotify.com/user/detalfulano",
        )

    def test_01_unauthorized(self):
        "User without token does not pass"
        response = self.client.get("/api/v1/suser/{0}/".format(
            self.user.user_id))
        self.assertEqual(response.status_code, 401)

    def test_02_get_user_info(self):
        "Get the user info"
        response = self.client.get("/api/v1/suser/{0}/?token={1}".format(
            self.user.user_id, self.token.token))
        self.assertEqual(response.status_code, 200)

    def test_03_create_user(self):
        "Get the user info on Spotify API and save on Database"
        self.client.get("/api/v1/suser/fernandochimi/?token={0}".format(
            self.token.token))
        new_user = create_user.delay("fernandochimi")
        self.assertTrue(new_user, "fernandochimi")

    def test_04_user_does_not_exist(self):
        "User does not exist"
        response = self.client.get(
            "/api/v1/suser/user-not-exist/?token={0}".format(self.token.token))
        self.assertEqual(response.status_code, 500)
