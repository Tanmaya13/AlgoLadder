# Generated by Django 2.2.14 on 2020-11-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_custom_user_referral_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom_user',
            name='referral_code',
            field=models.CharField(default='Generate Your Coupon Code', max_length=200),
        ),
    ]