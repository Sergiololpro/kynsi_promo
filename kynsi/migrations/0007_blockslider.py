# Generated by Django 3.0.3 on 2020-03-18 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kynsi', '0006_auto_20200318_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlockSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=256, verbose_name='Название блога')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Текст блока')),
                ('image', models.ImageField(blank=True, null=True, upload_to='site_images', verbose_name='Картинка блога')),
                ('is_show', models.BooleanField(default=True, verbose_name='Показывать элемент на сайте')),
            ],
            options={
                'verbose_name': 'Слайдер блога',
                'verbose_name_plural': 'Слайдер блога',
            },
        ),
    ]
