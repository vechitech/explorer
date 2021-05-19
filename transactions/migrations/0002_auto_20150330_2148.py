# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models 1DZNULrLKkQVHAZyrLhasfJGASpt9DV4kq migrations


class Migration(migrations.Migration):

    dependencies = [1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='onchaintransaction',
            old_name='conf_num',
            new_name='num_confs',
        ),
    ]
