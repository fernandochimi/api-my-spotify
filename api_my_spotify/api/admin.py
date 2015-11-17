# coding: utf-8
from django.contrib import admin

from models import ApiToken, SpotifyUser, SpotifyUserPlaylist


admin.site.register(ApiToken)
admin.site.register(SpotifyUser)
admin.site.register(SpotifyUserPlaylist)
