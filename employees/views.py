from django.db.models import Prefetch
from rest_framework import generics
from .models import Employee, Position, TeachDiscipline
from .serializers import EmployeeListSerializer, EmployeeDetailSerializer, PositionListWithEmployeesSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all().filter(is_active=True).select_related('position').only('last_name', 'first_name', 'middle_name',
                                                                      'ranks', 'position__name', 'image', 'slug')
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all().filter(is_active=True).select_related('position').prefetch_related(Prefetch('teach_disciplines',
                                                                                           queryset=TeachDiscipline.objects.only('name', 'description')))
    serializer_class = EmployeeDetailSerializer
    lookup_field = 'slug'


class PositionsWithEmployeesView(generics.ListAPIView):
    queryset = Position.objects.all().prefetch_related(
        Prefetch(
            'position_employees',
            queryset=Employee.objects.filter(is_active=True).only('last_name', 'first_name', 'middle_name', 'ranks', 'position', 'image',
                                           'slug')
        )
    )
    serializer_class = PositionListWithEmployeesSerializer


