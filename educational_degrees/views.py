from rest_framework import generics
from django.db.models import Prefetch
from employees.models import Employee
from .models import EducationalDegree, EducationalDegreeQualificationWorks, Subject, \
    EducationalDegreeDisciplinePrograms, QualificationWork
from .serializers import EducationalDegreeDetailedSerializer, EducationalDegreesSerializer, \
    QualificationWorksListSerializer, DisciplineProgramsListSerializer, DisciplineProgramsListSerializer2


class EducationalDegreeListView(generics.ListAPIView):
    queryset = EducationalDegree.objects.all()
    serializer_class = EducationalDegreesSerializer


class EducationalDegreeDetailView(generics.RetrieveAPIView):
    queryset = EducationalDegree.objects.all()
    serializer_class = EducationalDegreeDetailedSerializer
    lookup_field = 'slug'


class EducationalDegreeQualificationWorksByYearDetailView(generics.RetrieveAPIView):
    # /qualification_work/<slug:slug>
    queryset = EducationalDegreeQualificationWorks.objects.all().prefetch_related(
        Prefetch(
            'qualification_work',
            queryset=QualificationWork.objects.select_related('scientific_supervisor').select_related('scientific_supervisor__position').defer('scientific_supervisor__degree_history','scientific_supervisor__awards','scientific_supervisor__chosen_publications','scientific_supervisor__diploma_work_topics','scientific_supervisor__email', 'scientific_supervisor__image','scientific_supervisor__links','scientific_supervisor__ranks','scientific_supervisor__study_interests','scientific_supervisor__teach_disciplines','scientific_supervisor__time_created','scientific_supervisor__time_last_modified')
        )
    )
    serializer_class = QualificationWorksListSerializer
    lookup_field = 'slug'


class EducationalDegreeDisciplineProgramsByYearDetailView(generics.RetrieveAPIView):
    queryset = EducationalDegreeDisciplinePrograms.objects.all()
    serializer_class = DisciplineProgramsListSerializer2
    # serializer_class = DisciplineProgramsListSerializer
    lookup_field = 'slug'
