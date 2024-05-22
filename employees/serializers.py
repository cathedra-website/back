from rest_framework import serializers
from employees.models import Employee, Position, TeachDiscipline


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['name']


class TeachDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeachDiscipline
        fields = ['name', 'description']


class EmployeeListSerializer(serializers.ModelSerializer):
    position = PositionSerializer()

    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'middle_name', 'ranks', 'position', 'image', 'slug']
        # fields = 'all'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    teach_disciplines = TeachDisciplineSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = '__all__'
        lookup_field = 'slug'


class EmployeeShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['last_name', 'first_name', 'middle_name', 'slug']


class PositionListWithEmployeesSerializer(serializers.ModelSerializer):
    position_employees = EmployeeListSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = ('name', 'position_employees')