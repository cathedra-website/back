from django.urls import path
from .views import ScientificWorkTypeListView, ScientificWorkListView

app_name = 'library'

urlpatterns = [
    path('scientificworktypes/', ScientificWorkTypeListView.as_view(), name='scientific_work_types-list'),
    path('scientificworks/', ScientificWorkListView.as_view(), name='scientific_works-list')
]