from rest_framework import serializers

from employees.models import Employee
from library.models import ScientificWork, ScientificWorkType


class ScientificWorkTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificWorkType
        fields = ('name', 'slug')


class EmployeeSerializer(serializers.ModelSerializer):
    short_name = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ['short_name', 'slug']


class ScientificWorkSerializer(serializers.ModelSerializer):
    type = ScientificWorkTypeSerializer()
    workers = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = ScientificWork
        fields = '__all__'



