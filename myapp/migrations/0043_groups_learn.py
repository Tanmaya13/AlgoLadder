# Generated by Django 2.1.7 on 2021-05-01 10:07

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0042_auto_20210425_2208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups_learn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('questionsallotted', ckeditor.fields.RichTextField(blank=True, default='No Questions Allotted ! Mentors allot questions every week for practice according to learning pace of each individual student. Purchase a course to get a mentor assigned to you.', null=True)),
                ('link', models.URLField(blank=True)),
                ('group_members', models.ManyToManyField(blank=True, to='myapp.Custom_User')),
                ('mentor_alloted', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Mentor_user')),
            ],
        ),
    ]
