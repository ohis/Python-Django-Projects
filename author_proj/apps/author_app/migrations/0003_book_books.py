# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_app', '0002_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='books',
            field=models.ManyToManyField(to='author_app.Author'),
        ),
    ]