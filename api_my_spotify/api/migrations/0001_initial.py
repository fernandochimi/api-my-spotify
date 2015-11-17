# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiToken',
            fields=[
                ('token', models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, unique=True, verbose_name='token')),
                ('date_added', models.DateField(default=datetime.datetime(2015, 11, 17, 8, 52, 39, 651506), verbose_name='date added')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
            ],
        ),
    ]
