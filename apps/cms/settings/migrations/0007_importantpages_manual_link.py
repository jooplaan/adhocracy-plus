# Generated by Django 2.2.5 on 2019-09-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_cms_settings', '0006_importantpages_donate_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantpages',
            name='manual_link',
            field=models.URLField(blank=True),
        ),
    ]