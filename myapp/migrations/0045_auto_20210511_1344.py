# Generated by Django 2.1.7 on 2021-05-11 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0044_auto_20210508_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='courses',
            name='logo',
            field=models.ImageField(blank=True, upload_to='thumbnail/'),
        ),
        migrations.AddField(
            model_name='courses',
            name='structure',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='counter',
            field=models.CharField(default='1-0,2-0,4-0', max_length=20),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='mentors_alloted',
            field=models.ManyToManyField(blank=True, to='myapp.Mentor_user'),
        ),
    ]
