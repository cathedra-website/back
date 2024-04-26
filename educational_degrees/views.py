from rest_framework import generics
from .models import EducationalDegree
from .serializers import EducationalDegreeDetailedSerializer, EducationalDegreesSerializer


class EducationalDegreeListView(generics.ListAPIView):
    queryset = EducationalDegree.objects.all()
    serializer_class = EducationalDegreesSerializer


class EducationalDegreeDetailView(generics.RetrieveAPIView):
    queryset = EducationalDegree.objects.all()
    serializer_class = EducationalDegreeDetailedSerializer
    lookup_field = 'slug'
