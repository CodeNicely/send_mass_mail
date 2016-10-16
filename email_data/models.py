from __future__ import unicode_literals

from django.db import models

class user_data(models.Model):
	user_id= models.AutoField(primary_key=True)
	user_name=models.CharField(max_length=120,blank=True,null=True)
	user_emailid=models.CharField(max_length=120,unique=True)
	group_id=models.DecimalField(decimal_places=0, max_digits=10)

# Create your models here.
