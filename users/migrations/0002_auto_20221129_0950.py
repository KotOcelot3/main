# Generated by Django 3.2.16 on 2022-11-29 06:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='life_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 9, 50, 16, 830454), verbose_name='Время жизни'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 29, 9, 50, 16, 830435), verbose_name='Дата'),
        ),
    ]
