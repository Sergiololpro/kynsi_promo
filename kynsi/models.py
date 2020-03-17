from django.db import models

class Site(models.Model):
    """
    Модель основных настроек сайта
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

    pr_email = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Почта: 'Связь для прессы'",
        help_text="pr@kynsi.ru"
    )

    class Meta:
        verbose_name = "Основные настрйки сайта"
        verbose_name_plural = "Основные настрйки сайта"

class Salons(models.Model):
    """
    Модель салонов
    """
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название салона",
        help_text="KYNSI на Петровке"
    )

    short_title = models.CharField(
        max_length=64, null=False, blank=True, default="", verbose_name="Короткое название салона",
        help_text="Петровка"
    )

    address = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Адрес",
        help_text="Петровка 20/1"
    )

    time = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Часы работы",
        help_text="Без выходных, с 10:00 до 22:00"
    )

    phone = models.CharField(
        max_length=64, null=False, blank=True, default="", verbose_name="Телефон",
        help_text="+7 (495) 477-65-06"
    )

    image = models.ImageField(
        upload_to='site_images', null=True, blank=True,
        verbose_name="Картинка салона"
    )

    mango = models.CharField(
        max_length=32, null=False, blank=True, default="", verbose_name="Id салона для mango",
        help_text="11408"
    )

    reservi_id = models.CharField(
        max_length=32, null=False, blank=True, default="", verbose_name="Id салона для онлайн записи",
        help_text="2"
    )

    reservi_salon = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Код салона для онлайн записи",
        help_text="388236cd-fddf-11e6-b3ff-d05349e841da"
    )

    class Meta:
        verbose_name = "Салон"
        verbose_name_plural = "Салоны"

 