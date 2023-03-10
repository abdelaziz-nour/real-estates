# Generated by Django 4.1.7 on 2023-03-03 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realstateapp', '0011_alter_civil_registry_national_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=25)),
                ('nationalID', models.IntegerField()),
                ('type', models.CharField(choices=[('Land', 'Land'), ('Farm', 'Farm'), ('House', 'House'), ('Villa', 'Villa'), ('Store', 'Store'), ('Office', 'Office'), ('Building', 'Building'), ('Apartment', 'Apartment')], max_length=25)),
                ('operation', models.CharField(choices=[('Rent', 'Rent'), ('Sell', 'Sell')], max_length=25)),
                ('facilitiesNum', models.IntegerField()),
                ('state', models.CharField(max_length=25)),
                ('city', models.CharField(max_length=25)),
                ('location', models.TextField()),
                ('price', models.IntegerField()),
                ('approval', models.CharField(choices=[('Waiting', 'Waiting'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Waiting', max_length=25)),
                ('ownerShipProve', models.ImageField(upload_to=None)),
                ('image1', models.ImageField(upload_to=None)),
                ('image2', models.ImageField(upload_to=None)),
                ('image3', models.ImageField(upload_to=None)),
                ('advertiser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='civil_registry',
            new_name='CivilRegistry',
        ),
        migrations.RenameField(
            model_name='civilregistry',
            old_name='national_number',
            new_name='nationalID',
        ),
        migrations.RenameField(
            model_name='civilregistry',
            old_name='thired_name',
            new_name='third_name',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='national_number',
            new_name='nationalID',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='thired_name',
            new_name='third_name',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='password',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='username',
        ),
        migrations.DeleteModel(
            name='real_estate',
        ),
        migrations.AddField(
            model_name='image',
            name='realEstate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realstateapp.realestate'),
        ),
    ]
