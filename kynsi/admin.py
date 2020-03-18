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

@admin.register(Salons)
class Salons(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'short_title',
                    'address',
                    'time',
                    'phone',
                    'image',
                ]
            },  
        ),
        (
            'Mango', {
                'fields': [
                    'mango',
                ]
            },
        ),
        (
            'Онлайн запись', {
                'fields': [
                    'reservi_id',
                    'reservi_salon',
                ]
            },
        ),
    ]

@admin.register(Categories)
class Categories(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'order',
                    'is_show',
                ]
            },  
        ),
    ]

@admin.register(SubCategories)
class SubCategories(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'category',
                    'order',
                    'is_show',
                ]
            },  
        ),
    ]

@admin.register(Services)
class Services(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'subcategory',
                    'order',
                    'is_show',
                ]
            },  
        ),
    ]
