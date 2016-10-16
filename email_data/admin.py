from django.contrib import admin
from .models import *

class user_dataAdmin(admin.ModelAdmin):
	list_display=["user_id","user_name","user_emailid","group_id"]

admin.site.register(user_data,user_dataAdmin)

# Register your models here.
