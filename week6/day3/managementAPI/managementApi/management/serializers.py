from rest_framework import serializers
from .models import Department, Employee, Project, Task


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='department-detail')

    class Meta:
        model = Department
        fields = ['url', 'name', 'description']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'start_date', 'end_date']


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='employee-detail')
    department = serializers.HyperlinkedRelatedField(
        view_name='department-detail',
        queryset=Department.objects.all()
    )

    class Meta:
        model = Employee
        fields = ['url', 'name', 'email', 'phone_number', 'department']


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='task-detail')
    project = serializers.HyperlinkedRelatedField(
        view_name='project-detail',
        queryset=Project.objects.all()
    )

    class Meta:
        model = Task
        fields = ['url', 'name', 'description', 'due_date', 'completed', 'project']
