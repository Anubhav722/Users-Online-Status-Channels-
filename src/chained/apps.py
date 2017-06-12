from __future__ import unicode_literals

from django.apps import AppConfig


class ChainedConfig(AppConfig):
    name = 'chained'

    def ready(self):
    	import chained.signals