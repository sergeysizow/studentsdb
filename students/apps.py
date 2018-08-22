# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = u'База Студентів'

    def ready(self):
        import signals
        import colorize

