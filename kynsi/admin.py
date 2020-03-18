from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class SalonSliderImageInline(admin.TabularInline):
    model = SalonSliderImage
    extra = 3
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=200,
            height=150,
        ))

class InstaSliderImageInline(admin.TabularInline):
    model = InstaSliderImage
    extra = 3
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=200,
            height=150,
        ))

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
        (
            'Дополнительные', {
                'fields': [
                    'ya_map'
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
                    'image',
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
                    'price',
                    'order',
                    'is_show',
                ]
            },  
        ),
    ]

@admin.register(Brands)
class Brands(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'image'
                ]
            },  
        ),
    ]

@admin.register(SalonsSlider)
class SalonsSlider(admin.ModelAdmin):
    inlines = [SalonSliderImageInline]

@admin.register(InstaSlider)
class InstaSlider(admin.ModelAdmin):
    inlines = [InstaSliderImageInline]

@admin.register(BlogSlider)
class BlogSlider(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'text',
                    'image',
                    'is_show',
                ]
            },  
        ),
    ]


@admin.register(ReviewsSlider)
class ReviewsSlider(admin.ModelAdmin):
    model = Site
    extra = 0

    list_display = ('id', 'title')

    fieldsets = [
        (
            'Основные', {
                'fields': [
                    'title',
                    'text',
                    'image',
                    'is_show',
                ]
            },  
        ),
    ]
