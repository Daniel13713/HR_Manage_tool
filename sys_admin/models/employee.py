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
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import uuid
import pghistory
from sys_admin.models.base_model import BaseModel

class Employee(BaseModel, AbstractUser):
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
    email = models.EmailField(max_length=254)
    

    def __str__(self) -> str:
        return self.first_name
