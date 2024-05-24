from rest_framework import generics
from django.db.models import Prefetch
from employees.models import Employee
from .models import EducationalDegree, EducationalDegreeQualificationWorks, Subject, \
    EducationalDegreeDisciplinePrograms, QualificationWork, SubjectBlock
from .serializers import EducationalDegreeDetailedSerializer, EducationalDegreesSerializer, \
    QualificationWorksListSerializer, DisciplineProgramsListSerializer, SubjectBlockSerializer, \
    EducationalDegreeDisciplineProgramsSubjectBlocksSerializer


class EducationalDegreeListView(generics.ListAPIView):
    # return list of all educational degree with short description and slug
    queryset = EducationalDegree.objects.all().prefetch_related('detailed_info')
    serializer_class = EducationalDegreesSerializer


class EducationalDegreeDetailView(generics.RetrieveAPIView):
    # return detailed information about educational degree(with given slug)
    # detailed information includes lists of "кваліфікаціних робот", "програм навчальних дисциплін",
    # "навчальних планів", "описів освітніх програм" presented in form of lists
    queryset = EducationalDegree.objects.all().prefetch_related('detailed_info', 'study_plans', 'disciplines_programs')
    serializer_class = EducationalDegreeDetailedSerializer
    lookup_field = 'slug'


class EducationalDegreeQualificationWorksByYearDetailView(generics.RetrieveAPIView):
    # /qualification_work/<slug:slug>
    # return list of qualification works in the particular year(given in slug)
    queryset = EducationalDegreeQualificationWorks.objects.all().prefetch_related(
        Prefetch(
            'qualification_work',
            queryset=QualificationWork.objects.select_related('scientific_supervisor').select_related(
                'scientific_supervisor__position').defer('scientific_supervisor__degree_history',
                                                         'scientific_supervisor__awards',
                                                         'scientific_supervisor__chosen_publications',
                                                         'scientific_supervisor__diploma_work_topics',
                                                         'scientific_supervisor__email', 'scientific_supervisor__image',
                                                         'scientific_supervisor__links', 'scientific_supervisor__ranks',
                                                         'scientific_supervisor__study_interests',
                                                         'scientific_supervisor__teach_disciplines',
                                                         'scientific_supervisor__time_created',
                                                         'scientific_supervisor__time_last_modified')
        )
    )
    serializer_class = QualificationWorksListSerializer
    lookup_field = 'slug'


class EducationalDegreeDisciplineProgramsByYearDetailView(generics.RetrieveAPIView):
    # discipline_programs/<slug:slug>
    # return list of disciplines in the particular year
    # list sorted by semester of disciplines

    queryset = EducationalDegreeDisciplinePrograms.objects.all()
    serializer_class = DisciplineProgramsListSerializer
    lookup_field = 'slug'


class EducationalDegreeDisciplineProgramsSubjectBlocksView(generics.RetrieveAPIView):
    # discipline_programs/<slug:slug>/subject-blocks
    # return list of blocks for the given year(slug)
    queryset = EducationalDegreeDisciplinePrograms.objects.all()
    serializer_class = EducationalDegreeDisciplineProgramsSubjectBlocksSerializer
    lookup_field = 'slug'

# class DisciplineProgramsBlocksListView(generics.ListAPIView):
#     queryset = SubjectBlock.objects.all()
#     serializer_class = SubjectBlockSerializer
