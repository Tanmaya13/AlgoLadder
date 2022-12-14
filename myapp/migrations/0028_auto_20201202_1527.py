# Generated by Django 2.1.7 on 2020-12-02 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_auto_20201124_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='date1',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='courses',
            name='date2',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='courses',
            name='date3',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='courses',
            name='date4',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='courses',
            name='seat1',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AddField(
            model_name='courses',
            name='seat2',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AddField(
            model_name='courses',
            name='seat3',
            field=models.IntegerField(blank=True, default=10),
        ),
        migrations.AddField(
            model_name='courses',
            name='seat4',
            field=models.IntegerField(blank=True, default=10),
        ),
    ]
