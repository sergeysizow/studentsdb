# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 14:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_student_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='\u0414\u0438\u0441\u0446\u0438\u043f\u043b\u0456\u043d\u0430')),
                ('date', models.DateTimeField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0432\u0435\u0434\u0435\u043d\u043d\u044f')),
                ('teacher', models.CharField(max_length=256, verbose_name='\u0412\u0438\u043a\u043b\u0430\u0434\u0430\u0447')),
                ('location', models.IntegerField(verbose_name='\u0410\u0443\u0434\u0438\u0442\u043e\u0440\u0456\u044f')),
                ('notes', models.TextField(blank=True, verbose_name='\u0414\u043e\u0434\u0430\u0442\u043a\u043e\u0432\u0456 \u043d\u043e\u0442\u0430\u0442\u043a\u0438')),
                ('student_group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='students.Group', verbose_name='\u0413\u0440\u0443\u043f\u0430')),
            ],
            options={
                'verbose_name': ('\u0415\u043a\u0437\u0430\u043c\u0435\u043d',),
                'verbose_name_plural': '\u0415\u043a\u0437\u0430\u043c\u0435\u043d\u0438',
            },
        ),
    ]