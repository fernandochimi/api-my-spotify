# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20151117_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apitoken',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2015, 11, 18, 8, 57, 12, 78077), verbose_name='date added'),
        ),
        migrations.AlterField(
            model_name='spotifyuser',
            name='followers',
            field=models.IntegerField(null=True, verbose_name='followers', blank=True),
        ),
        migrations.AlterField(
            model_name='spotifyuser',
            name='name',
            field=models.CharField(max_length=250, null=True, verbose_name='name', blank=True),
        ),
    ]
