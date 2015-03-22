# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dane',
            fields=[
                ('id', models.AutoField(
                    verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(
                    max_length=300, verbose_name=b'ukradziony url')),
                ('type', models.CharField(default=b'p', max_length=1,
                                          verbose_name=b'Type zapytania HTTP', choices=[(b'p', b'POST'), (b'g', b'GET')])),
                ('data', models.TextField(verbose_name=b'Tresc zapytania')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
