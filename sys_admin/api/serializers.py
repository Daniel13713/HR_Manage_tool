from record.models.education import Education
from sys_admin.models.employee import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):

    # Add field with relationship with other tables
    roles = serializers.StringRelatedField(many=True)
    resume = serializers.StringRelatedField()
    education = serializers.SlugRelatedField(
        read_only=True,
        slug_field="education_title"
    )

    class Meta:
        model = Employee
        fields = '__all__' # Add all fields