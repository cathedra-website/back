from django.urls import path, include
from rest_framework import routers

from . import views
from .views import (EducationalDegreeListView, EducationalDegreeDetailView,
                    EducationalDegreeQualificationWorksByYearDetailView,
                    EducationalDegreeDisciplineProgramsByYearDetailView,
                    EducationalDegreeDisciplineProgramsSubjectBlocksView)

app_name = 'educational_degrees'

urlpatterns = [
    path('', EducationalDegreeListView.as_view(), name='educational-degrees-list'),
    path('<slug:slug>/', EducationalDegreeDetailView.as_view(), name='educational-degrees-detail'),
    path('qualification_work/<slug:slug>', EducationalDegreeQualificationWorksByYearDetailView.as_view(),
         name='educational-degrees-qualification-works-by-year'),
    path('discipline_programs/<slug:slug>', EducationalDegreeDisciplineProgramsByYearDetailView.as_view(),
         name='educational-degrees-discipline-programs'),
    path('discipline_programs/<slug:slug>/subject-blocks/', EducationalDegreeDisciplineProgramsSubjectBlocksView.as_view(),
     name='discipline-program-subject-blocks'),
    # path('blocks', DisciplineProgramsBlocksListView.as_view(),
    #      name='discipline-programs-blocks'),
]
