# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagelets', '0013_page_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelet',
            name='css_parent',
            field=models.CharField(blank=True, max_length=255, help_text='Extra CSS classes, if any, to be added to the pikatainer DIV in the HTML.', null=True, verbose_name='Parent CSS classes'),
            preserve_default=True,
        ),
    ]
