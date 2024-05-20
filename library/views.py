import math

from django.core.exceptions import BadRequest
from django.db.models import Q, Prefetch
from rest_framework import pagination
from rest_framework import generics
from rest_framework.filters import BaseFilterBackend
from rest_framework.response import Response

from employees.models import Employee
from library.models import ScientificWork, ScientificWorkType
from .serializers import ScientificWorkTypeSerializer, ScientificWorkSerializer


class ScientificWorkTypeListView(generics.ListAPIView):
    queryset = ScientificWorkType.objects.all()
    serializer_class = ScientificWorkTypeSerializer


class ScientificWorkPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'limit'
    max_page_size = 15

    def get_paginated_response(self, data):
        return Response({
            'total_pages': self.page.paginator.num_pages,
            'total_items': self.page.paginator.count,
            'current_page': self.page.number,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class ScientificWorkListView(generics.ListAPIView):
    queryset = ScientificWork.objects.all().select_related('type').prefetch_related(Prefetch(
            'workers',
            queryset=Employee.objects.only('last_name', 'slug')
        ))
    serializer_class = ScientificWorkSerializer
    pagination_class = ScientificWorkPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        name_query_parameter = self.request.query_params.get('name')
        type_query_parameter = self.request.query_params.get('type')

        if name_query_parameter and type_query_parameter:
            queryset = queryset.filter(
                (Q(name__icontains=name_query_parameter) | Q(isbn__exact=name_query_parameter)) &
                Q(type__slug=type_query_parameter)
            )
        elif name_query_parameter and not type_query_parameter:
            queryset = queryset.filter(Q(name__icontains=name_query_parameter) | Q(isbn__exact=name_query_parameter))
        elif type_query_parameter and not name_query_parameter:
            queryset = queryset.filter(Q(type__slug=type_query_parameter))

        return queryset



