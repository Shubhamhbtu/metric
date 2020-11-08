from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class MyData(models.Model):
    create_date = models.DateTimeField(_("Created At"), auto_now_add=True)
    input_list = ArrayField(models.IntegerField(null=True, blank=True,),
                            null=True, blank=True, size=5)

    def __str__(self):
        return str(self.create_date)
