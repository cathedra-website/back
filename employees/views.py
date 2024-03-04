from rest_framework import generics
from .models import Employee
from .serializers import EmployeeListSerializer, EmployeeDetailSerializer


class EmployeeListView(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeListSerializer


class EmployeeDetailView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeDetailSerializer
    lookup_field = 'slug'
