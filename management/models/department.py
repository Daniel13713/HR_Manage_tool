#!/usr/bin/python3

"""
--------------------------
Deparment Data Model
--------------------------
"""

from email.policy import default
from secrets import choice
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
import pghistory
from sys_admin.models.base_model import BaseModel
from sys_admin.models.employee import Employee

class Department(BaseModel):
    """
    ----------------------------------
    Create Table in Postgres Database
    ----------------------------------
    """
    
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Employee_Department(BaseModel):
    """
    ----------------------------------
    Many-to-Many relationship between
    Employee and Department tables
    ----------------------------------
    """

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    start_date = models.DateTimeField(
        help_text="Date when employee start in department",
        default=timezone.now
    )
    end_date = models.DateTimeField(
        help_text="Date when employee end in department",
        default=timezone.now
    )

    def __str__(self) -> str:
        return "{}-{}".format(self.employee.__str__(), self.department.__str__())