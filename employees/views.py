from rest_framework import generics
from .models import Employee, Position
from .serializers import EmployeeListSerializer, EmployeeDetailSerializer, PositionListWithEmployeesSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all().select_related('position')
    serializer_class = EmployeeDetailSerializer
    lookup_field = 'slug'


class PositionsWithEmployeesView(generics.ListAPIView):
    queryset = Position.objects.all().prefetch_related('position_employees')
    serializer_class = PositionListWithEmployeesSerializer


