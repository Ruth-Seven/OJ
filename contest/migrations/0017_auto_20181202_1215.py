# Generated by Django 2.1.3 on 2018-12-02 12:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0016_auto_20181202_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='endtime',
            field=models.DateField(default=datetime.datetime(2018, 12, 2, 17, 15, 12, 581831), verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 12, 15, 12, 581803), verbose_name='比赛开始时间'),
        ),
    ]
