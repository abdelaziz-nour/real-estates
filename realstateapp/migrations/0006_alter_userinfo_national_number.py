# Generated by Django 4.1.7 on 2023-02-24 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0005_rename_addvertiser_national_number_real_estate_adds_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='national_number',
            field=models.IntegerField(unique=True),
        ),
    ]