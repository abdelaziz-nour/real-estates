# Generated by Django 4.1.7 on 2023-02-24 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='civil_registry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('thired_name', models.CharField(max_length=25)),
                ('forth_name', models.CharField(max_length=25)),
                ('national_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='real_estate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estate_name', models.CharField(max_length=25)),
                ('estate_number', models.IntegerField()),
                ('owner_national_number', models.IntegerField()),
                ('estate_type', models.CharField(choices=[('apartment for rent', 'apartment for rent'), ('apartment for sell', 'apartment for sell'), ('house for rent', 'house for rent'), ('house for sell', 'house for sell'), ('villa for rent', 'villa for rent'), ('villa for sell', 'villa for sell'), ('land for sell', 'land for sell'), ('bulding for sell', 'building for sell'), ('store for rent', 'store for rent'), ('office for rent', 'office for rent')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='real_estate_adds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('addvertiser_national_number', models.IntegerField()),
                ('estate_number', models.IntegerField()),
                ('estate_type', models.CharField(choices=[('apartment for rent', 'apartment for rent'), ('apartment for sell', 'apartment for sell'), ('house for rent', 'house for rent'), ('house for sell', 'house for sell'), ('villa for rent', 'villa for rent'), ('villa for sell', 'villa for sell'), ('land for sell', 'land for sell'), ('bulding for sell', 'building for sell'), ('store for rent', 'store for rent'), ('office for rent', 'office for rent')], max_length=25)),
                ('number_of_facilities', models.IntegerField()),
                ('location', models.TextField()),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='userInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('second_name', models.CharField(max_length=25)),
                ('thired_name', models.CharField(max_length=25)),
                ('forth_name', models.CharField(max_length=25)),
                ('national_number', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('username', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=25)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
