from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have a valid email address.')

        if not kwargs.get('username'):

            raise ValueError('Users must have a valid username.')

        account = self.model(
        email=self.normalize_email(email), username=kwargs.get('username')
        )
        account.is_staff=False
        account.set_password(password)
        account.save()
        return account

    def create_superuser(self,email,password,**kwargs):
        account = self.create_user(email, password, **kwargs)
        account.is_staff = True
        account.is_admin = True
        account.save()

        return account


class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, primary_key=True, null=False)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    is_admin = models.BooleanField(default=False)
    is_staff= models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

    gender_choices = (
        ('m', 'Male'),
        ('f', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=gender_choices,)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
