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

    ya_map = models.TextField(
        max_length=256, null=False, blank=True, default="", verbose_name="src из яндекс карт",
        help_text="https://yandex.ru/map-widget/v1/?um=constructor%3Ac2cc93efc49dcd1f934e880248f1c3531200eb3a94cc165c483d659df6bb1630&amp;source=constructor"
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


class Categories(models.Model):
    """
    Модель категорий
    """
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название категории",
        help_text="Маникюры"
    )

    image = models.ImageField(
        upload_to='site_images', null=True, blank=True,
        verbose_name="Картинка услуги"
    )

    order = models.IntegerField(verbose_name="Порядок отображения категорию", default=100)

    is_show = models.BooleanField(
        verbose_name="Показывать категорию на сайте", default=True,
    )

    class Meta:
        verbose_name = "Услуги - категории"
        verbose_name_plural = "Услуги - категории"

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        return ' -> '.join(full_path[::-1])

    @property
    def get_subcategories(self):
         return SubCategories.objects.filter(category=self.id, is_show=True)


class SubCategories(models.Model):
    """
    Модель подкатегорий
    """
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название подкатегории",
        help_text="Маникюры"
    )

    category = models.ForeignKey(Categories, verbose_name='Родительская категория', related_name='parent', on_delete=models.CASCADE)

    order = models.IntegerField(verbose_name="Порядок отображения подкатегорию", default=100)

    is_show = models.BooleanField(
        verbose_name="Показывать подкатегорию на сайте", default=True,
    )

    class Meta:
        verbose_name = "Услуги - подкатегории"
        verbose_name_plural = "Услуги - подкатегории"

    def __str__(self):                           
        full_path = [self.title]                  
        k = self.parent
        return ' -> '.join(full_path[::-1])

    @property
    def get_sevices(self):
         return Services.objects.filter(subcategory=self.id, is_show=True)


class Services(models.Model):
    """
    Модель услуги
    """
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название услуги",
        help_text="Маникюры"
    )

    subcategory = models.ForeignKey(SubCategories, verbose_name='Родительская подкатегория', related_name='parent', on_delete=models.CASCADE)

    price = models.CharField(
        max_length=8, null=False, blank=True, default="", verbose_name="Цена",
        help_text="4000"
    )

    order = models.IntegerField(verbose_name="Порядок отображения подкатегорию", default=100)

    is_show = models.BooleanField(
        verbose_name="Показывать услугу на сайте", default=True,
    )

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"


class Brands(models.Model):
    """
    Модель брендов
    """
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название бренда",
        help_text="Kure BAZAAR"
    )

    image = models.ImageField(
        upload_to='site_images', null=True, blank=True,
        verbose_name="Картинка бренда"
    )

    is_show = models.BooleanField(
        verbose_name="Показывать бренд на сайте", default=True,
    )

    class Meta:
        verbose_name = "Бренды"
        verbose_name_plural = "Бренды"


class SalonsSlider(models.Model):
    """
    Модель слайдера салонов
    """
    class Meta:
        verbose_name = "Слайдер салонов"
        verbose_name_plural = "Слайдер салонов"


class SalonSliderImage(models.Model):
    """
    Модель картинок слайдера салонов
    """
    image = models.ImageField('Картинки', upload_to='site_images', null=True)
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название картинки слайдера",
        help_text="Kynsi Петровка"
    )
    salonslider = models.ForeignKey(SalonsSlider, verbose_name='Слайдер салона', related_name='images', on_delete=models.CASCADE)
    ordering = models.IntegerField('Порядок', default=0)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Картинка для сладйера салонов'
        verbose_name_plural = 'Картинка для сладйера салонов'
        ordering = ['ordering']


class InstaSlider(models.Model):
    """
    Модель слайдера instagram
    """
    class Meta:
        verbose_name = "Слайдер instagram"
        verbose_name_plural = "Слайдер instagram"


class InstaSliderImage(models.Model):
    """
    Модель картинок слайдера салонов
    """
    image = models.ImageField('Картинки', upload_to='site_images', null=True)
    url = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Сслыка на пост в insagram",
        help_text="https://www.instagram.com/p/BpM7dqQHUmz/"
    )
    title = models.CharField(
        max_length=128, null=False, blank=True, default="", verbose_name="Название картинки слайдера",
        help_text="Kynsi Петровка"
    )
    slider = models.ForeignKey(InstaSlider, verbose_name='Слайдер insagram', related_name='images', on_delete=models.CASCADE)
    ordering = models.IntegerField('Порядок', default=0)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Картинка для сладйера instagram'
        verbose_name_plural = 'Картинка для сладйера instagram'
        ordering = ['ordering']


class BlogSlider(models.Model):
    """
    Модель слайдера блогов
    """
    title = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Заголовок блога",
    )

    text = models.TextField('Текст блока', null=True, blank=True, help_text="Абзацы в &lt;p&gt;&lt;/p&gt;")

    image = models.ImageField(
        upload_to='site_images', null=True, blank=True,
        verbose_name="Картинка блога"
    )

    is_show = models.BooleanField(
        verbose_name="Показывать элемент на сайте", default=True,
    )

    class Meta:
        verbose_name = "Слайдер блога"
        verbose_name_plural = "Слайдер блога"


class ReviewsSlider(models.Model):
    """
    Модель слайдера отзывов
    """
    title = models.CharField(
        max_length=256, null=False, blank=True, default="", verbose_name="Заголовок отзыва",
    )

    text = models.TextField('Текст отзыва', null=True, blank=True, help_text="Абзацы в &lt;p&gt;&lt;/p&gt;")

    image = models.ImageField(
        upload_to='site_images', null=True, blank=True,
        verbose_name="Картинка отзыва"
    )

    is_show = models.BooleanField(
        verbose_name="Показывать элемент на сайте", default=True,
    )

    class Meta:
        verbose_name = "Слайдер отзывов"
        verbose_name_plural = "Слайдер отзывов"

 