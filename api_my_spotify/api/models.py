# coding: utf-8
import uuid

from datetime import datetime

from django.db import models


class ApiToken(models.Model):
    token = models.UUIDField(
        u'token', default=uuid.uuid4, unique=True, primary_key=True)
    date_added = models.DateField(u'date added', default=datetime.now())
    is_active = models.BooleanField(u'active', default=True)
