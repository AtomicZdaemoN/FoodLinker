from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

# This module contains all the models for the accounts and authentication
class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'address', 'phone']

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'users'


class Provider(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=255)
    is_license_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name

    class Meta:
        db_table = 'providers'

class Charity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    registration_id = models.CharField(max_length=100, unique=True)  # If registered in Official Government Database
    is_verified = models.BooleanField(default=False)  # If the charity is verified by the system
    food_types = models.CharField(max_length=255, help_text="Types of food they can handle (e.g., perishable, non-perishable, both)")
    capacity = models.IntegerField(help_text="Maximum food quantity (in kilograms) they can store")

    def __str__(self):
        return self.user.name

    class Meta:
        db_table = 'charities'