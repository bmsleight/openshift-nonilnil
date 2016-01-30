# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_auto_20160126_2259'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medal',
            options={'ordering': ['medal_date']},
        ),
        migrations.AlterField(
            model_name='medal',
            name='tag',
            field=models.CharField(choices=[('Gold', 'Gold - Winning a series'), ('Silver', 'Silver - Comming 2nd'), ('Bronze', 'Bronze - 3rd in a series'), ('90', '90 - Goal in times added on (not extra time) to avoid nil nil'), ('TopGoal', 'TopGoal - Picked the game out of all the possible games with the highest number of goals'), ('AFC', 'AFC - Picked AFC Wimbledon in a game they won'), ('Bomb', 'Bomb - Out in the first week'), ('Warning', 'Warning - Lost because of a rule volalation'), ('Postpone', 'Postpone - Lost becasue of a postponed game'), ('Twitter', 'Twitter - Followed @NoNilNil on twitter'), ('Group', 'Group - Introduced NoNilNil, to someone outside of TI'), ('Globe', 'Globe - Introduced NoNilNil, to someone outside of the UK')], blank=True, max_length=10, null=True),
        ),
    ]
