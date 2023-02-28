from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class userInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    first_name = models.CharField(max_length=25, blank=False, null=False)
    second_name = models.CharField(max_length=25, blank=False, null=False)
    thired_name = models.CharField(max_length=25, blank=False, null=False)
    forth_name = models.CharField(max_length=25, blank=False, null=False)
    national_number = models.IntegerField(blank=False, null=False, unique=True)
    phone = models.IntegerField(blank=False, null=False)
    email = models.CharField(max_length=25, blank=False, null=False)
    username = models.CharField(max_length=25, blank=False, null=False)
    password = models.CharField(max_length=25, blank=False, null=False)
    state = models.CharField(max_length=25, blank=False, null=False)
    city = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self,):
        return str(self.user.username)


class civil_registry(models.Model):
    first_name = models.CharField(max_length=25, blank=False, null=False)
    second_name = models.CharField(max_length=25, blank=False, null=False)
    thired_name = models.CharField(max_length=25, blank=False, null=False)
    forth_name = models.CharField(max_length=25, blank=False, null=False)
    national_number = models.IntegerField(blank=False, null=False)

    def __str__(self,):
        return str(self.first_name)


class real_estate(models.Model):
    addvertiser = models.ForeignKey(User, on_delete=models.CASCADE)
    estate_name = models.CharField(max_length=25, blank=False, null=False)
    authentication_image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    estate_description = models.CharField(
        max_length=25, blank=False, null=False)
    owner_national_number = models.IntegerField(blank=False, null=False)
    estate_types = [('apartment for rent', 'apartment for rent'),
                    ('apartment for sell', 'apartment for sell'),
                    ('house for rent', 'house for rent'),
                    ('house for sell', 'house for sell'),
                    ('villa for rent', 'villa for rent'),
                    ('villa for sell', 'villa for sell'),
                    ('land for sell', 'land for sell'),
                    ('bulding for sell', 'building for sell'),
                    ('store for rent', 'store for rent'),
                    ('office for rent', 'office for rent'),
                    ]
    estate_type = models.CharField(
        max_length=25, blank=False, null=False, choices=estate_types)
    number_of_facilities = models.IntegerField(blank=False, null=False)
    state = models.CharField(max_length=25, blank=False, null=False)
    city = models.CharField(max_length=25, blank=False, null=False)
    location = models.TextField(blank=False, null=False)
    optional_details = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    estate_statuses = [('Waitting', 'Waitting'),
                       ('Accepted', 'Accepted'),
                       ('Rejected', 'Rejected')
                       ]
    estate_status = models.CharField(
        max_length=25, blank=False, null=False, choices=estate_statuses, default="Waitting")
    estate_image1 = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    estate_image2 = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    estate_image3 = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None)
    map_location = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self,):
        return str(self.estate_name)
