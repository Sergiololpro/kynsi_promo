# Generated by Django 3.0.3 on 2020-03-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kynsi', '0002_brands'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brands',
            options={'verbose_name': 'Бренды', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AddField(
            model_name='brands',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='Показывать бренд на сайте'),
        ),
    ]
