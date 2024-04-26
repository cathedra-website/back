from rest_framework import serializers
from educational_degrees.models import (EducationalDegree, EducationalDegreeDetailsFiles,
                                        EducationalDegreeStudyProgramsFiles, EducationalDegreeStudyPlansFiles,
                                        EducationalDegreeDisciplineProgramsFiles,
                                        EducationalDegreeQualificationWorksFiles)


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


class DisciplineProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeDisciplineProgramsFiles
        fields = ['name', "file"]


class QualificationWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalDegreeQualificationWorksFiles
        fields = ['name', "file"]


class EducationalDegreeDetailedSerializer(serializers.ModelSerializer):
    study_programs_desc = StudyProgramsSerializer(many=True, read_only=True)
    study_plans = StudyPlansSerializer(many=True, read_only=True)
    disciplines_programs = DisciplineProgramsSerializer(many=True, read_only=True)
    qualification_works = QualificationWorksSerializer(many=True, read_only=True)

    class Meta:
        model = EducationalDegree
        lookup_field = 'slug'
        fields = ['name', "description", "slug",
                  "study_programs_desc", "study_plans", "disciplines_programs", "qualification_works"
                  ]


class EducationalDegreesSerializer(serializers.ModelSerializer):
    detailed_info = DetailedInfoSerializer(many=True, read_only=True)

    class Meta:
        model = EducationalDegree
        fields = ['name', "description", "slug", "detailed_info"]
