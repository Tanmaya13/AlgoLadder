# Generated by Django 2.1.7 on 2020-09-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_interviewexperiences_companyname'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='fullname',
            field=models.CharField(default='fullname', max_length=200),
        ),
    ]
