from rest_framework import serializers
from collections import defaultdict
from educational_degrees.models import (EducationalDegree, EducationalDegreeDetailsFiles,
                                        EducationalDegreeStudyProgramsFiles, EducationalDegreeStudyPlansFiles,
                                        EducationalDegreeDisciplinePrograms, Subject, SubjectBlock,
                                        EducationalDegreeQualificationWorks,
                                        QualificationWork)
from employees.serializers import EmployeeShortSerializer


class DetailedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeDetailsFiles
        fields = ['name', "file"]


class StudyProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeStudyProgramsFiles
        fields = ['name', "file"]


class StudyPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeStudyPlansFiles
        fields = ['name', "file"]


class DisciplineProgramsShortListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeDisciplinePrograms
        fields = ['year', "slug"]


class SubjectBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectBlock
        fields = ['name', 'full_name']


class SubjectSerializer(serializers.ModelSerializer):
    block = SubjectBlockSerializer(read_only=True)

    class Meta:
        model = Subject
        fields = ['name', 'semester', 'block']


class DisciplineProgramsListSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = EducationalDegreeDisciplinePrograms
        lookup_field = 'slug'
        fields = ['year', "slug", "subjects", 'degree_name', ]


class QualificationWorksSerializer(serializers.ModelSerializer):
    scientific_supervisor = EmployeeShortSerializer(read_only=True)

    class Meta:
        model = QualificationWork
        fields = ['full_name', "topic_of_work", "scientific_supervisor"]


class QualificationWorksShortListSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeQualificationWorks
        fields = ['year', "slug"]


class QualificationWorksListSerializer(serializers.ModelSerializer):
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


class DisciplineProgramsListSerializer2(serializers.ModelSerializer):
    subjects_by_semester = serializers.SerializerMethodField()

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