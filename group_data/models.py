from __future__ import unicode_literals

from django.db import models

class group_data(models.Model):
	group_id=models.SmallIntegerField(primary_key=True)
	group_name=models.CharField(max_length=120, blank=True, null=True)
# Create your models here.
