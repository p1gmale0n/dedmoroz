# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-19 12:03
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_remove_letter_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Контент на главной',
                'verbose_name_plural': 'Контенты на главной',
            },
        ),
    ]
