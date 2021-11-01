import datetime

from django.contrib.auth.models import User
from django.contrib.gis.db import models

from onadata.apps.logger.models.xform import XForm


class XFormSubmissionCounter(models.Model):
    user = models.ForeignKey(
        User,
        related_name='xformsubmissioncounter',
        null=True,
        on_delete=models.CASCADE,
    )
    xform = models.ForeignKey(
        XForm,
        related_name='xformcounter',
        null=True,
        on_delete=models.CASCADE,
    )
    count = models.IntegerField(default=0)
    timestamp = models.DateField()

    class Meta:
        unique_together = ('xform', 'timestamp')

    def save(self, *args, **kwargs):
        if not self.timestamp:
            today = datetime.date.today()
            first_day_of_month = today.replace(day=1)
            self.timestamp = first_day_of_month

        super().save(*args, **kwargs)
