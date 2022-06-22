#!/usr/bin/python3

"""
--------------------------
Base Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from turtle import update
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory

class BaseModel(models.Model):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(default=timezone.now, editable=False)
    update_at = models.DateTimeField(default=timezone.now, editable=False)
    status = models.BooleanField(default=True)

    class Meta:
        abstract = True
