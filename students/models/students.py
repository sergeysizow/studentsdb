from django.db import models
from django.utils.translation import ugettext_lazy as _
#from .groups import Group


class Student(models.Model):
    """ Students model """

    # user-friendly name in admin

    class Meta(object):
        verbose_name = _("Student"),
        verbose_name_plural = _("Students")

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("First name")
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Last name")
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=_("Middle name"),
        default=''
    )

    birthday = models.DateField(
        blank=False,
        verbose_name=_("Birthday"),
        null=True
    )

    photo = models.ImageField(
        blank=True,
        verbose_name=_("Photo"),
        null=True
    )

    ticket = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Ticket")
    )

    notes = models.TextField(
        blank=True,
        verbose_name=_("Extra notes")
    )

    student_group = models.ForeignKey(
        'Group',
        verbose_name=_("Group"),
        blank=False,
        null=True,
        on_delete=models.PROTECT
    )

    # change name students in admin for human))
    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
