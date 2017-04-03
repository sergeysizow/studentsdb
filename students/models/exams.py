# _*_ coding: utf-8 _*_

from __future__ import unicode_literals

from django.db import models



class Exam(models.Model):
    """ Examen model """

    # user-frendly name in admin

    class Meta(object):
        verbose_name = u"Екзамен",
        verbose_name_plural = u"Екзамени"

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Дисципліна")
    
    date = models.DateTimeField(
        blank=False,
        verbose_name=u"Дата проведення",
        null=True)
    
    teacher = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Викладач")
  
    student_group = models.ForeignKey(
        'Group',
        verbose_name=u"Група",
        blank=False,
        null=True,
        on_delete=models.PROTECT)

    location =models.IntegerField(
	verbose_name=u"Аудиторія",
	null=False)

    notes = models.TextField(
        blank=True,
        verbose_name=u"Додаткові нотатки")

    # chandge name examens in admin for human))
    def __unicode__(self):
        return u"%s %s" % (self.title, self.student_group)

