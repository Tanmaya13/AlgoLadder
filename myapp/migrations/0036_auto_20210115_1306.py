# Generated by Django 2.1.7 on 2021-01-15 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_time_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time_slot',
            name='from_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]