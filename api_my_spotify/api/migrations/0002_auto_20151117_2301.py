# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyUser',
            fields=[
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('user_id', models.CharField(max_length=128, unique=True, serialize=False, verbose_name='user id', primary_key=True)),
                ('followers', models.IntegerField(verbose_name='followers')),
                ('picture', models.URLField(max_length=250, null=True, verbose_name='picture path', blank=True)),
                ('link', models.URLField(max_length=250, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Spotify User',
                'verbose_name_plural': 'Spotify Users',
            },
        ),
        migrations.CreateModel(
            name='SpotifyUserPlaylist',
            fields=[
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('link', models.URLField(max_length=250, verbose_name='url')),
                ('playlist_id', models.CharField(max_length=128, unique=True, serialize=False, verbose_name='playlist id', primary_key=True)),
                ('user', models.ForeignKey(to='api.SpotifyUser')),
            ],
            options={
                'verbose_name': 'Spotify User Playlist',
                'verbose_name_plural': 'Spotify Users Playlists',
            },
        ),
        migrations.AlterModelOptions(
            name='apitoken',
            options={'verbose_name': 'API Token', 'verbose_name_plural': 'API Tokens'},
        ),
        migrations.AlterField(
            model_name='apitoken',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 11, 17, 23, 1, 14, 462824), verbose_name='date added'),
        ),
    ]
