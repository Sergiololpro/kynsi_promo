# Generated by Django 3.0.3 on 2020-03-18 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kynsi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', help_text='Kure BAZAAR', max_length=128, verbose_name='Название бренда')),
                ('image', models.ImageField(blank=True, null=True, upload_to='site_images', verbose_name='Картинка бренда')),
            ],
        ),
    ]
