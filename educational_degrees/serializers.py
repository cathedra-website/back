from rest_framework import serializers
from collections import defaultdict
from educational_degrees.models import (EducationalDegree, EducationalDegreeDetailsFiles,
                                        EducationalDegreeStudyProgramsFiles, EducationalDegreeStudyPlansFiles,
                                        EducationalDegreeDisciplinePrograms, Subject, SubjectBlock,
                                        EducationalDegreeQualificationWorks,
                                        QualificationWork)
from employees.models import Employee


class DetailedInfoSerializer(serializers.ModelSerializer):
    # "Детальна інформація"
    class Meta:
        model = EducationalDegreeDetailsFiles
        fields = ['name', "file"]


class StudyProgramsSerializer(serializers.ModelSerializer):
    # "Описи освітніх програм"
    class Meta:
        model = EducationalDegreeStudyProgramsFiles
        fields = ['name', "file"]


class StudyPlansSerializer(serializers.ModelSerializer):
    # "Навчальні плани"
    class Meta:
        model = EducationalDegreeStudyPlansFiles
        fields = ['name', "file"]


class DisciplineProgramsShortListSerializer(serializers.ModelSerializer):
    # "Програми навчальних дисциплін"
    # list with short info about discipline programs
    class Meta:
        model = EducationalDegreeDisciplinePrograms
        fields = ['year', "slug"]


class SubjectBlockSerializer(serializers.ModelSerializer):
    # "Програми навчальних дисциплін"
    class Meta:
        model = SubjectBlock
        fields = ['name', 'full_name']


class SubjectSerializer(serializers.ModelSerializer):
    # "Програми навчальних дисциплін"
    block = SubjectBlockSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = ['name', 'semester', 'block']


class DisciplineProgramsListSerializer(serializers.ModelSerializer):
    # "Програми навчальних дисциплін"
    subjects_by_semester = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = EducationalDegreeDisciplinePrograms
        lookup_field = 'slug'
        fields = ['year', "slug", "subjects_by_semester", 'degree_name']

    def get_subjects_by_semester(self, obj):
        subjects = obj.subjects.all()
        grouped_subjects = defaultdict(list)

        for subject in subjects:
            semester = subject.semester
            grouped_subjects[semester].append({
                'name': subject.name,
                'semester': subject.semester,
                'block': {
                    'name': subject.block.name,
                    'full_name': subject.block.full_name
                }
            })

        return dict(sorted(grouped_subjects.items()))

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Group subjects by semester
        representation['subjects'] = representation.pop('subjects_by_semester')
        return representation


class EducationalDegreeDisciplineProgramsSubjectBlocksSerializer(serializers.ModelSerializer):
    # "Програми навчальних дисциплін"
    subject_blocks = serializers.SerializerMethodField()

    class Meta:
        model = EducationalDegreeDisciplinePrograms
        fields = ['year', 'slug', 'degree_name', 'subject_blocks']

    def get_subject_blocks(self, obj):
        subjects = obj.subjects.all()
        subject_blocks = SubjectBlock.objects.filter(subject_block__in=subjects).distinct()
        return SubjectBlockSerializer(subject_blocks, many=True).data

class EmployeeShortSerializer(serializers.ModelSerializer):
    # "Кваліфікаційні роботи"
    short_name_with_position = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = ('short_name_with_position', 'slug', 'is_active')


class QualificationWorksSerializer(serializers.ModelSerializer):
    # "Кваліфікаційні роботи"
    scientific_supervisor = EmployeeShortSerializer(read_only=True)

    class Meta:
        model = QualificationWork
        fields = ['full_name', "topic_of_work", "scientific_supervisor"]


class QualificationWorksShortListSerializer(serializers.ModelSerializer):
    # "Кваліфікаційні роботи"
    class Meta:
        model = EducationalDegreeQualificationWorks
        fields = ['year', "slug"]


class QualificationWorksListSerializer(serializers.ModelSerializer):
    # "Кваліфікаційні роботи"
    qualification_work = QualificationWorksSerializer(many=True, read_only=True)

    class Meta:
        model = EducationalDegreeQualificationWorks
        lookup_field = 'slug'
        fields = ['year', "slug", "qualification_work", 'degree_name', ]


class EducationalDegreeDetailedSerializer(serializers.ModelSerializer):
    study_programs_desc = StudyProgramsSerializer(many=True, read_only=True)
    study_plans = StudyPlansSerializer(many=True, read_only=True)
    disciplines_programs = DisciplineProgramsShortListSerializer(many=True, read_only=True)
    qualification_works = QualificationWorksShortListSerializer(many=True, read_only=True)

    class Meta:
        model = EducationalDegree
        lookup_field = 'slug'
        fields = ['name', "description", "slug",
                  "study_programs_desc", "study_plans",
                  "disciplines_programs",
                  "qualification_works"
                  ]


class EducationalDegreesSerializer(serializers.ModelSerializer):
    detailed_info = DetailedInfoSerializer(many=True, read_only=True)

    class Meta:
        model = EducationalDegree
        fields = ['name', "description", "slug", "detailed_info"]

