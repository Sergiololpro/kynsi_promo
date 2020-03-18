# Generated by Django 3.0.3 on 2020-03-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kynsi', '0009_auto_20200318_0825'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=256, verbose_name='Заголовок отзыва')),
                ('text', models.TextField(blank=True, help_text='Абзацы в &lt;p&gt;&lt;/p&gt;', null=True, verbose_name='Текст отзыва')),
                ('image', models.ImageField(blank=True, null=True, upload_to='site_images', verbose_name='Картинка отзыва')),
                ('is_show', models.BooleanField(default=True, verbose_name='Показывать элемент на сайте')),
            ],
            options={
                'verbose_name': 'Слайдер отзывов',
                'verbose_name_plural': 'Слайдер отзывов',
            },
        ),
        migrations.AlterField(
            model_name='blockslider',
            name='title',
            field=models.CharField(blank=True, default='', max_length=256, verbose_name='Заголовок блога'),
        ),
    ]
