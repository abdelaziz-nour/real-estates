# Generated by Django 4.1.7 on 2023-03-03 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('realstateapp', '0014_rename_first_name_civilregistry_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='realestate',
            old_name='ownerShipProve',
            new_name='ownerShipProof',
        ),
    ]
