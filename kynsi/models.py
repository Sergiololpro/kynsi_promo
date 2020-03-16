from django.db import models

class Site(models.Model):
    """
    Модель основных настроек сайта.
    """
    seo_title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Seo title",
        help_text="Kynsi"
    )

    seo_description = models.CharField(
        max_length=1024, null=False, blank=True, default="", verbose_name="Seo title",
        help_text="Салоны KYNSI: Сити, Петровка, Патриаршие | Маникюр и педикюр Christina Fitzgerald, La Ric | Укладки и окрашивание"
    )

    vk = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Вконтакте",
        help_text="https://vk.com/kynsi"
    )

    facebook = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Facebook",
        help_text="https://www.facebook.com/kynsi.salon"
    )

    instagram = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Instagram",
        help_text="https://www.instagram.com/kynsisalon/"
    )

    q_email = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Почта: 'Вопросы и предложения'",
        help_text="hello@kynsi.ru"
    )

    work_email = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Почта: 'Работайте с нами'",
        help_text="work@kynsi.ru"
    )

    q_email = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Почта: 'Связь для прессы'",
        help_text="pr@kynsi.ru"
    )

    class Meta:
        verbose_name = "Основные настрйки сайта"
        verbose_name_plural = "Основные настрйки сайта"

 