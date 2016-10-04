# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0014_pagelet_css_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelet',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='content'),
            preserve_default=True,
        ),
    ]
