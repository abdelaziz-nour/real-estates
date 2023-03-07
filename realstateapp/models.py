from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    firstName = models.CharField(max_length=25, blank=False, null=False)
    secondName = models.CharField(max_length=25, blank=False, null=False)
    thirdName = models.CharField(max_length=25, blank=False, null=False)
    forthName = models.CharField(max_length=25, blank=False, null=False)

    nationalID = models.CharField(max_length=16, blank=False, null=False, unique=True)
    phone = models.CharField(max_length=16, blank=False, null=False, unique=True)
    state = models.CharField(max_length=25, blank=False, null=False)
    city = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self,):
        return str(self.firstName + " " + self.forthName)


class CivilRegistry(models.Model):
    firstName = models.CharField(max_length=25, blank=False, null=False)
    secondName = models.CharField(max_length=25, blank=False, null=False)
    thirdName = models.CharField(max_length=25, blank=False, null=False)
    forthName = models.CharField(max_length=25, blank=False, null=False)
    nationalID = models.CharField(max_length=16, blank=False, null=False, unique=True)

    def __str__(self,):
        return str(self.firstName + " " + self.forthName)


class RealEstate(models.Model):
    advertiser = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, blank=False, null=False)
    description = models.TextField(max_length=512, blank=False, null=False)
    nationalID = models.IntegerField(blank=False, null=False)

    types = [
        ('Land', 'Land'),
        ('Farm', 'Farm'),
        ('House', 'House'),
        ('Villa', 'Villa'),
        ('Store', 'Store'),
        ('Office', 'Office'),
        ('Building', 'Building'),
        ('Apartment', 'Apartment'),
    ]
    type = models.CharField(max_length=25, blank=False, null=False, choices=types)

    operations = [('Rent', 'Rent'), ('Sell', 'Sell'), ]
    operation = models.CharField(max_length=25, blank=False, null=False, choices=operations)

    facilitiesNum = models.IntegerField(blank=False, null=False)
    state = models.CharField(max_length=25, blank=False, null=False)
    city = models.CharField(max_length=25, blank=False, null=False)
    location = models.TextField(blank=False, null=False)
    price = models.IntegerField(blank=False, null=False)

    approval_states = [('Waiting', 'Waiting'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')]
    approval = models.CharField(max_length=25, blank=False, null=False, choices=approval_states, default="Waiting")

    def __str__(self):
        return str(self.title)


class Image(models.Model):
    realEstate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    types = [("Proof", "Proof"), ("View", "View")]
    type = models.CharField(max_length=8, blank=False, null=False, choices=types, default="View")

    def __str__(self):
        return str(self.realEstate.title + " - " + str(self.realEstate.pk))
