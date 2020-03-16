from django.contrib import admin
from .models import *


@admin.register(Site)
class SiteSettings(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'seo_title')

