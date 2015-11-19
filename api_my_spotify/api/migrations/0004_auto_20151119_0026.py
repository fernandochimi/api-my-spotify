# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20151118_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotifyuserplaylist',
            name='user',
        ),
        migrations.AlterField(
            model_name='apitoken',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 11, 19, 0, 26, 35, 919257), verbose_name='date added'),
        ),
        migrations.DeleteModel(
            name='SpotifyUserPlaylist',
        ),
    ]
