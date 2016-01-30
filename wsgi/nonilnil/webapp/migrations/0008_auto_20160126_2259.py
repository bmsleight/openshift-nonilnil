# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_medal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medal',
            name='medal_date',
            field=models.DateField(verbose_name='Date games will be played on'),
        ),
    ]
