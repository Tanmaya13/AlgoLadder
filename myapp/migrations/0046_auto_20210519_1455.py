# Generated by Django 2.1.7 on 2021-05-19 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_auto_20210511_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='logo',
            field=models.ImageField(default='default.jpg', upload_to='blogs_pics/'),
        ),
        migrations.AddField(
            model_name='interviewexperiences',
            name='logo',
            field=models.ImageField(default='default.jpg', upload_to='interview_pics/'),
        ),
    ]