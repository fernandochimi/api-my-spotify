# coding: utf-8
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = "api"
    verbose_name, verbose_name_plural = "API", "APIs"

    def ready(self):
        self.get_models()
