from rest_framework import generics
from .models import EducationalDegree, EducationalDegreeQualificationWorks
from .serializers import EducationalDegreeDetailedSerializer, EducationalDegreesSerializer, \
    QualificationWorksListSerializer


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
