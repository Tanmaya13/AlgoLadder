# Generated by Django 2.1.7 on 2021-03-03 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0008_auto_20201203_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='codingsubmissions',
            name='contest',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contest.Contests'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='codingsubmissions',
            name='marks_obtained',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='contests',
            name='check',
            field=models.CharField(default='Public', max_length=100),
        ),
        migrations.AddField(
            model_name='contests',
            name='contraint',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='contests',
            name='leaderboard',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='contests',
            name='runcode',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='codingsubmissions',
            name='result',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
