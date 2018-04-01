from django.contrib import admin

# Register your models here.
from .models import Hdd, Facility

admin.site.register(Hdd)
admin.site.register(Facility)