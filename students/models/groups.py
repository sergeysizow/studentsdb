# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models
from .students import Student


class Group(models.Model):
    """ Groups model """

    # user-friendly name in admin

    class Meta(object):
        verbose_name = u"Група",
        verbose_name_plural = u"Групи"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Назва")

    leader = models.OneToOneField(
        Student,
        verbose_name=u"Староста",
        blank=True,
        null=True,

        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    # change name students in admin for human))
    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,
                                    self.leader.last_name)
        else:
            return u"%s" % (self.title,)
