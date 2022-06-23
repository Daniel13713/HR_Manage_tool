from sys_admin.models.employee import Employee
from management.models.role import Employee_Role
from rest_framework import viewsets, permissions
from sys_admin.api.serializers import EmployeeSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action

# Lead Viewset


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = EmployeeSerializer

    employees = Employee.objects.all()
    #employees_roles = Employee_Role.objects.all()
    #print(employees_roles)
    #print([Employee.objects.get(id=employee_role.employee_id) for employee_role in employees_roles])
    queryset = employees

    @action(detail=True, methods=["GET"], url_path='roles')
    def roles(self, request, pk=None):
        employee = self.get_object()
        roles = employee.roles.all()
        return Response([role.name for role in roles])

    