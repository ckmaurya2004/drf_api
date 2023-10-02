from django.contrib import admin
from .models import *

# Register your models here.,ProductLine

class ProductLineInlineAdmin(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductLineInlineAdmin]

admin.site.register((Brand,Category))