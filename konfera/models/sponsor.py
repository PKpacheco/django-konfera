from django.db import models
from django.utils.translation import ugettext_lazy as _

from konfera.models.abstract import KonferaModel


class Sponsor(KonferaModel):
    SPONSOR_TYPE = (
        (1, _('Platinum')),
        (2, _('Gold')),
        (3, _('Silver')),
        (4, _('Bronze')),
        (5, _('Other')),
        (6, _('Django girls')),
    )

    title = models.CharField(max_length=128)
    type = models.IntegerField(choices=SPONSOR_TYPE)
    logo = models.FileField()
    url = models.URLField()
    about_us = models.TextField(blank=True)

    def __str__(self):
        return self.title
