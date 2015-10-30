# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20151030_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='membership',
            name='status',
            field=models.IntegerField(default=0, choices=[(0, b'Applying'), (1, b'Approved'), (2, b'Denied')]),
        ),
    ]
