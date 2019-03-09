from django.db import models
from accounts.models import User

# Create your models here.

class Address(models.Model):
    id = models.AutoField(primary_key=True, blank=False, auto_created=True, max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    addressline = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    area = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(max_length=150)
    pincode = models.CharField(max_length=150)
    country = models.CharField(max_length=150)

class venue(models.Model):
    id = models.AutoField(primary_key=True, blank=False, max_length=150, auto_created=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    capacity = models.CharField(max_length=150)
    ac = models.BooleanField(default=False)
    contactno = models.CharField(max_length=150, unique=True)
    address = models.ForeignKey(to=Address, on_delete=models.CASCADE)
    cost = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

class Catering(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no=models.CharField(max_length=150,unique=True)
    address_id=models.ForeignKey(to=Address,on_delete=models.CASCADE,blank=False)
    foodtype_choices = (('veg', 'Veg'), ('nonveg', 'Non-Veg'))
    foodtype=models.CharField(max_length=10,choices=foodtype_choices)

class MenuImage(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    catering=models.ForeignKey(to=Catering,on_delete=models.CASCADE)
    image=models.ImageField(blank=False,upload_to='Menu',default='')


class invitation(models.Model):
    id = models.AutoField(primary_key=True, max_length=150)
    event = models.ForeignKey(to=Address, max_length=100, on_delete=models.SET_NULL, null=True)
    needprinted = models.BooleanField(default=False)
    iscustomized = models.BooleanField(default=False)


class Profile(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    contact=models.CharField(max_length=12,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,upload_to='ProfilePics',default='')
    gender_choices = (('m', 'Male'),('f', 'Female'),('o','other'))
    gender = models.CharField(max_length=10, choices=gender_choices)








# class decorationservice

class events(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, max_length=150)
    user=models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    venue = models.ForeignKey(venue, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(blank=False)
    starttime = models.DateTimeField(blank=False)
    endtime = models.DateTimeField(blank=False)
    expected_people = models.CharField(max_length=150, blank=False)
    confirmed_people = models.CharField(max_length=150, blank=False)