# coding: utf-8
from django.contrib import admin

from models import ApiToken, SpotifyUser


class ApiTokenAdmin(admin.ModelAdmin):
    list_display = ("token", "date_added", "is_active")
    search_fields = ["token", ]
    list_filter = ("is_active", )


class SpotifyUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "name", "followers")
    search_fields = ["name", "user_id", ]

admin.site.register(ApiToken, ApiTokenAdmin)
admin.site.register(SpotifyUser, SpotifyUserAdmin)
