from django.db import models
from .students import Student
from django.utils.translation import ugettext_lazy as _


class Group(models.Model):
    """ Groups model """

    # user-friendly name in admin

    class Meta(object):
        verbose_name = _("Group")
        verbose_name_plural = _("Groups")

    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_("Title"))

    leader = models.OneToOneField(
        Student,
        verbose_name= _("Leader"),
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    notes = models.TextField(
        blank=True,
        verbose_name=_("Extra notes"))

    # change name students in admin for human))
    def __unicode__(self):
        if self.leader:
            return u"%s (%s %s)" % (self.title, self.leader.first_name,
                                    self.leader.last_name)
        else:
            return u"%s" % (self.title,)
