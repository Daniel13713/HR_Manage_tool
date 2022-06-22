from django.contrib import admin
from sys_admin.models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Employee, UserAdmin)