# Generated by Django 2.1.7 on 2021-02-26 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_auto_20210225_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='method_type',
            field=models.CharField(default='Not Purchased', max_length=20),
        ),
    ]
