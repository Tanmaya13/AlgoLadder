# Generated by Django 2.1.7 on 2020-12-03 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0005_auto_20201025_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='contests',
            name='image_link',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
