from django.db import models
from accounts.models import User
from django.shortcuts import reverse

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
    image= models.ImageField(null=True,default='',upload_to="venueimage")
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    capacity = models.CharField(max_length=150)
    ac_choice=(('ac',"A/C"),('non-ac','Non A/c'))
    ac = models.CharField(max_length=10,choices=ac_choice)
    contact_no = models.CharField(max_length=150, unique=False)
    cost = models.CharField(max_length=150)
    #is_active = models.BooleanField(default=True)
    name = models.CharField(blank=False, max_length=150,default='Name of Venue')
    Addressline = models.CharField(max_length=150,default="Enter Address")
    street = models.CharField(max_length=150,default="Enter Street")
    area = models.CharField(max_length=150,default="Enter Area")
    city = models.CharField(max_length=150,default="Enter City")
    state = models.CharField(max_length=150,default="Enter state")
    pincode = models.CharField(max_length=150,default="Enter pincode")
    country = models.CharField(max_length=150,default="country")
    def get_absolute_url(self):
        return reverse('venue-detail', args=[str(self.id)])

class SoundSystem(models.Model):
    id = models.AutoField(primary_key=True, blank=False, max_length=150, auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=150, unique=False)
    #address_id = models.ForeignKey(to=Address, on_delete=models.CASCADE, blank=False)
    cost = models.CharField(max_length=150)
    # is_active = models.BooleanField(default=True)
    name = models.CharField(blank=False, max_length=150, default='Name of Venue')
    Addressline = models.CharField(max_length=150, default="Enter Address")
    street = models.CharField(max_length=150, default="Enter Street")
    area = models.CharField(max_length=150, default="Enter Area")
    city = models.CharField(max_length=150, default="Enter City")
    state = models.CharField(max_length=150, default="Enter state")
    pincode = models.CharField(max_length=150, default="Enter pincode")
    country = models.CharField(max_length=150, default="country")
    def get_absolute_url(self):
        return reverse('seller-SoundSystem-detail', args=[str(self.id)])

class Catering(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    contact_no=models.CharField(max_length=150,unique=False)
    cost=models.CharField(max_length=150,default='')
    foodtype_choices = (('veg', 'Veg'), ('nonveg', 'Non-Veg'))
    foodtype=models.CharField(max_length=10,choices=foodtype_choices)
    name = models.CharField(blank=False, max_length=150, default='')
    Addressline = models.CharField(max_length=150, default="")
    street = models.CharField(max_length=150, default="")
    area = models.CharField(max_length=150, default="")
    city = models.CharField(max_length=150, default="")
    state = models.CharField(max_length=150, default="")
    pincode = models.CharField(max_length=150, default="")
    country = models.CharField(max_length=150, default="")

    def get_absolute_url(self):
        return reverse('seller-Catering-detail', args=[str(self.id)])


class MenuImage(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    catering=models.ForeignKey(to=Catering,on_delete=models.CASCADE)
    image=models.ImageField(blank=False,upload_to='Menu',default='')


class Decoration(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=150, unique=False)
    # address_id = models.ForeignKey(to=Address, on_delete=models.CASCADE, blank=False)
    cost = models.CharField(max_length=150)
    # is_active = models.BooleanField(default=True)
    name = models.CharField(blank=False, max_length=150, default='Name of Venue')
    Addressline = models.CharField(max_length=150, default="Enter Address")
    street = models.CharField(max_length=150, default="Enter Street")
    area = models.CharField(max_length=150, default="Enter Area")
    city = models.CharField(max_length=150, default="Enter City")
    state = models.CharField(max_length=150, default="Enter state")
    pincode = models.CharField(max_length=150, default="Enter pincode")
    country = models.CharField(max_length=150, default="country")

    def get_absolute_url(self):
        return reverse('seller-Decoration-detail', args=[str(self.id)])


class invitation(models.Model):
    id = models.AutoField(primary_key=True, max_length=150)
    event = models.ForeignKey(to=Address, max_length=100, on_delete=models.SET_NULL, null=True)
    needprinted = models.BooleanField(default=False)
    iscustomized = models.BooleanField(default=False)


class Profile(models.Model):
    id=models.AutoField(primary_key=True,blank=False,max_length=150,auto_created=True)
    last_name = models.CharField(max_length=20, blank=True)
    contact=models.CharField(max_length=12,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,upload_to='ProfilePics',default='')
    gender_choices = (('m', 'Male'),('f', 'Female'),('o','other'))
    gender = models.CharField(max_length=10, choices=gender_choices)
    first_name=models.CharField(max_length=20,blank=True)









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