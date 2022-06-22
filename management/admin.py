from django.contrib import admin

from management.models import *
# Register your models here.

admin.site.register([
    Department,
    Role,
    Report,
    Team,
    Employee_Department,
    Employee_Role,
    Employee_Team,
    Employee_Report,
])