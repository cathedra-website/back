from django.db.models import Prefetch
from rest_framework import generics
from .models import Employee, Position
from .serializers import EmployeeListSerializer, EmployeeDetailSerializer, PositionListWithEmployeesSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all().select_related('position')
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all().select_related('position').prefetch_related('teach_disciplines')
    serializer_class = EmployeeDetailSerializer
    lookup_field = 'slug'


class PositionsWithEmployeesView(generics.ListAPIView):
    queryset = Position.objects.all().prefetch_related(
        Prefetch(
            'position_employees',
            queryset=Employee.objects.only('last_name', 'first_name', 'middle_name', 'ranks', 'position', 'image',
                                           'slug')
        )
    )
    serializer_class = PositionListWithEmployeesSerializer


