from rest_framework import routers
from sys_admin.api.views import EmployeeViewSet
from django.conf.urls import path, include

router = routers.DefaultRouter()
router.register('employees', EmployeeViewSet, 'employees')

urlpatterns = [
    path("", include(router.urls), name="employees")
]