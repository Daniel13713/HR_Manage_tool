#!/usr/bin/python3

"""
--------------------------
Employee-user Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager, UserManager, AbstractBaseUser
from django.utils import timezone
import uuid
import pghistory
from sys_admin.models.base_model import BaseModel
import pgtrigger

class EmployeeManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        -------------------------------------
        Creates and saves a User with the 
        given email, identifier and password.
        -------------------------------------
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an Username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        """
        ------------------------------
        Creates and saves a superuser
        with the given email, identifier
        and password.
        ------------------------------
        """
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Employee(BaseModel, AbstractBaseUser):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    last_name_second = models.CharField(max_length=100, blank=True)
    identifier = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)
    username = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    data_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True, editable=False)
    last_login = models.DateTimeField(verbose_name="date joined", auto_now=True, editable=False)

    gender_options = [
        ('F', 'Female'),
        ('M', 'Male'),
        ('NB', 'Not Binary'),
    ]
    gender = models.CharField(max_length=10, choices=gender_options, default='NB')

    # Many to Many Relationships
    #from management.models.department import Department
    

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['email']
    
    objects = EmployeeManager()

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True
