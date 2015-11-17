# coding: utf-8
from django.test import TestCase

from .factories import ApiTokenFactory


class ApiTokenTest(TestCase):
    def setUp(self):
        self.token = ApiTokenFactory()
