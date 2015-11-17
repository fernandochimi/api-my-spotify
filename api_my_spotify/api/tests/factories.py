# coding: utf-8
import factory

from api.models import ApiToken


class ApiTokenFactoru(factory.django.DjangoModelFactory):
    class Meta:
        model = ApiToken
