# Generated by Django 2.1.7 on 2021-01-15 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0034_auto_20210109_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time_Slot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.TimeField()),
                ('mentor', models.ManyToManyField(blank=True, to='myapp.Mentor_user')),
            ],
        ),
    ]