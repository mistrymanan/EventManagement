from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

class User(AbstractUser):
    #gender = models.CharField(max_length=100,default='')
    def __str__(self):
        return '{username} [{email}]'.format(username=self.username, email=self.email)