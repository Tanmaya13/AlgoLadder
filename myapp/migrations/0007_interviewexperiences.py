# Generated by Django 2.1.7 on 2020-04-30 05:55

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_note_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterviewExperiences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=500)),
                ('linkofauthor', models.CharField(default='', max_length=200)),
            ],
        ),
    ]
