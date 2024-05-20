from rest_framework import generics
from .models import EducationalDegree, EducationalDegreeQualificationWorks, Subject, EducationalDegreeDisciplinePrograms
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
    queryset = EducationalDegreeQualificationWorks.objects.all()
    serializer_class = QualificationWorksListSerializer
    lookup_field = 'slug'


class EducationalDegreeDisciplineProgramsByYearDetailView(generics.RetrieveAPIView):
    queryset = EducationalDegreeDisciplinePrograms.objects.all()
    serializer_class = DisciplineProgramsListSerializer2
    # serializer_class = DisciplineProgramsListSerializer
    lookup_field = 'slug'
