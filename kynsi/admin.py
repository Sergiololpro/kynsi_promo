from django.contrib import admin
from .models import *


@admin.register(Site)
class SiteSettings(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'seo_title')

    fieldsets = [
        (
            'Seo', {
                'fields': [
                    'seo_title',
                    'seo_description',
                ]
            },  
        ),
        (
            'Социальные сети', {
                'fields': [
                    'vk',
                    'facebook',
                    'instagram',
                ]
            },
        ),
        (
            'Почтовые ящики', {
                'fields': [
                    'q_email',
                    'work_email',
                    'pr_email',
                ]
            },
        ),
    ]

