# Generated by Django 2.1.7 on 2020-04-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200406_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='universitycgpa',
            field=models.IntegerField(default=0),
        ),
    ]
