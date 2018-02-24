from django.contrib import admin
from attendance.models import Session
from . import models
# Register your models here.

class SessionAdmin(admin.ModelAdmin):

    list_filter = ['user','session','t_date']
    list_display = ['user','session','t_date']


admin.site.register(Session,SessionAdmin)
