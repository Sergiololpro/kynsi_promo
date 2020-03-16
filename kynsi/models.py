from django.db import models

class Site(models.Model):
    """
    Модель основных настроек сайта.
    """
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название сайта",
        help_text="Например, Courchevel 1850"
    )