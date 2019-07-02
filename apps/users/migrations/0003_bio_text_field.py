# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('liqd_product_users', '0003_bio_text_field')]

    dependencies = [
        ('a4_candy_users', '0002_add-user-fields-for-profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=255, verbose_name='Biography'),
        ),
    ]