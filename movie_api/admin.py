from django.contrib import admin
from . models import WatchList,PlatForm,Review

# Register your models here.
admin.site.register((WatchList,PlatForm,Review))