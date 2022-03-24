from datetime import timedelta

from django.db import models
from django.utils.translation import gettext as _


class Parking(models.Model):
    created = models.DateTimeField(
        _("Created at"), auto_now_add=True, auto_now=False
    )
    updated = models.DateTimeField(
        _("Updated at"), auto_now_add=False, auto_now=True
    )
    plate = models.CharField(_("Plate"), max_length=8, null=False)
    time = models.DurationField(_("Time"), null=False, default=timedelta())
    paid = models.BooleanField(_("Paid"), default=False, null=False)
    left = models.BooleanField(_("Left"), default=False, null=False)

    class Meta:
        db_table = "parking"
