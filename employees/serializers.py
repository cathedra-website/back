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
        # fields = '__all__'


class EmployeeDetailSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    teach_disciplines = TeachDisciplineSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'
        lookup_field = 'slug'

