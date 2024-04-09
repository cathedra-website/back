from django.urls import path, include
from rest_framework import routers

from . import views
from .views import EmployeeListView, EmployeeDetailView, PositionsWithEmployeesView

app_name = 'employees'

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('positionswithemployees/', PositionsWithEmployeesView.as_view(), name='positions'),
    path('<slug:slug>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
