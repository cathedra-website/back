from django.urls import path, include
from rest_framework import routers

from . import views
from .views import EducationalDegreeListView, EducationalDegreeDetailView

app_name = 'educational_degrees'

urlpatterns = [
    path('', EducationalDegreeListView.as_view(), name='educational-degrees-list'),
    path('<slug:slug>/', EducationalDegreeDetailView.as_view(), name='educational-degrees-detail'),

]
