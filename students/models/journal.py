# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from .students import Student
from .groups import Group

import calendar

v = calendar.Calendar(firstweekday=0)


class Journal(models.Model):
    """ Students model """

    # user-frendly name in admin

    class Meta(object):
        verbose_name = u"Журнал",
        verbose_name_plural = u"Журнали"

    name = models.ForeignKey(
        Student,
        verbose_name=u"Студент",
        blank=False,
        null=False,
    )

    group = models.OneToOneField(
        Group,
        verbose_name=u"Група",
        blank=False,
        null=False,
    )

    for date in v.itermonthdays(2017, 4):
        date = models.NullBooleanField(
            verbose_name=u"дата",
            default=True)

    # change name in admin for human))
    def __unicode__(self):
        return u"%s %s" % (self.name, self.group)
