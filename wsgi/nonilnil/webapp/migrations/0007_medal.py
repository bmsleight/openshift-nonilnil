# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0006_auto_20160111_1941'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medal',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('tag', models.CharField(null=True, choices=[('Gold', 'Gold - Winning a series'), ('Silver', 'Silver - Comming 2nd'), ('Bronze', 'Bronze - 3rd in a series'), ('AFC', 'AFC - Picked AFC Wimbledon in a game they won')], blank=True, max_length=10)),
                ('medal_date', models.DateTimeField(verbose_name='Date games will be played on')),
                ('description', models.TextField(verbose_name='Glory description')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
