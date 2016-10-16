from django.contrib import admin
from .models import *

class group_dataAdmin(admin.ModelAdmin):
	list_display=["group_id","group_name"]

admin.site.register(group_data,group_dataAdmin)

# Register your models here.
