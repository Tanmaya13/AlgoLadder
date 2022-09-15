# Generated by Django 2.1.7 on 2021-07-20 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_algoedge_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='ask_doubt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=200)),
                ('doubt', models.CharField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='custom_user',
            name='AlgoEdge_enrolled',
            field=models.BooleanField(default=False),
        ),
    ]
