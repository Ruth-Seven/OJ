# Generated by Django 2.1.3 on 2018-12-02 11:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0009_auto_20181202_1003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest_problem',
            name='accepted_num',
        ),
        migrations.RemoveField(
            model_name='contest_problem',
            name='contest_problem_id',
        ),
        migrations.RemoveField(
            model_name='contest_problem',
            name='submit_num',
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='accepted',
            field=models.IntegerField(default=0, verbose_name='通过人数'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='题目添加时间'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='description',
            field=models.TextField(blank=True, verbose_name='题目描述'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='hint',
            field=models.TextField(blank=True, verbose_name='题目提示'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='input_decscription',
            field=models.TextField(blank=True, verbose_name='输入描述'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='memory_limit',
            field=models.IntegerField(default=65536, verbose_name='内存限制'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='memory_limit_other',
            field=models.IntegerField(default=32768, verbose_name='其他语言内存限制'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='output_decscription',
            field=models.TextField(blank=True, verbose_name='输出描述'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='sample_input',
            field=models.TextField(blank=True, verbose_name='样例输入'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='sample_output',
            field=models.TextField(blank=True, verbose_name='样例输出'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='source',
            field=models.CharField(blank=True, max_length=200, verbose_name='题目来源'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='submitted',
            field=models.IntegerField(default=0, verbose_name='提交人数'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='time_limit_C',
            field=models.IntegerField(default=1000, verbose_name='时间限制'),
        ),
        migrations.AddField(
            model_name='contest_problem',
            name='time_limit_other',
            field=models.IntegerField(default=2000, verbose_name='其他语言限制'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='endtime',
            field=models.DateField(default=datetime.datetime(2018, 12, 2, 16, 25, 24, 218034), verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='starttime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 2, 11, 25, 24, 218002), verbose_name='比赛开始时间'),
        ),
        migrations.AlterField(
            model_name='contest_problem',
            name='problem_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='题目编号'),
        ),
        migrations.AlterField(
            model_name='contest_problem',
            name='title',
            field=models.CharField(blank=True, max_length=1000, verbose_name='题目标题'),
        ),
    ]
