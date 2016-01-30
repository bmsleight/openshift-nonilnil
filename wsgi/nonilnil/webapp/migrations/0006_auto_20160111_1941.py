# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_auto_20160109_2210'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nilnils',
            options={'ordering': ['round_f']},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['series']},
        ),
        migrations.AlterModelOptions(
            name='prediction',
            options={'ordering': ['round_f']},
        ),
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['-round_date']},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='payment',
            name='payment',
            field=models.DecimalField(max_digits=5, default=5, decimal_places=2),
        ),
    ]
