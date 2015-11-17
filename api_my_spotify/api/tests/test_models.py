# coding: utf-8
from django.test import TestCase

from .factories import ApiTokenFactory


class ApiTokenTest(TestCase):
    def setUp(self):
        self.token = ApiTokenFactory()

    def test_01_unicode(self):
        self.assertEqual(unicode(self.token), u'{0}'.format(self.token.token))
