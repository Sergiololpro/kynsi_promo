# Generated by Django 3.0.3 on 2020-03-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kynsi', '0008_auto_20200316_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='salons',
            name='short_title',
            field=models.CharField(blank=True, default='', help_text='Петровка', max_length=64, verbose_name='Короткое название салона'),
        ),
    ]