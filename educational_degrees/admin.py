import json

from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.safestring import mark_safe

from .models import (EducationalDegree, EducationalDegreeDetailsFiles, EducationalDegreeDisciplineProgramsFiles,
                     EducationalDegreeStudyProgramsFiles, EducationalDegreeStudyPlansFiles,
                     EducationalDegreeQualificationWorks, QualificationWork)


@admin.register(EducationalDegree)
class EducationalDegreeAdmin(admin.ModelAdmin):
    fields = ("name", "description", "slug", "qualification_works", "disciplines_programs", "study_plans",
              "study_programs_desc", "detailed_info")
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)

    readonly_fields = ('slug',)


@admin.register(EducationalDegreeDetailsFiles)
class EducationalDegreeDetailsFilesAdmin(admin.ModelAdmin):
    fields = ("name", "file",)
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)

@admin.register(EducationalDegreeStudyProgramsFiles)
class EducationalDegreeStudyProgramsFilesAdmin(admin.ModelAdmin):
    fields = ("name", "file",)
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)

@admin.register(EducationalDegreeDisciplineProgramsFiles)
class EducationalDegreeDisciplineProgramsFilesAdmin(admin.ModelAdmin):
    fields = ("name", "file",)
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)

@admin.register(EducationalDegreeStudyPlansFiles)
class EducationalDegreeStudyPlansFilesAdmin(admin.ModelAdmin):
    fields = ("name", "file",)
    list_display = ('name',)
    list_per_page = 10
    search_fields = ('name',)

@admin.register(EducationalDegreeQualificationWorks)
class EducationalDegreeQualificationWorksFilesAdmin(admin.ModelAdmin):
    fields = ("year", "qualification_work", 'degree_name', 'slug',)
    list_display = ('year',)
    list_per_page = 10
    search_fields = ('year',)

    readonly_fields = ('slug',)

@admin.register(QualificationWork)
class QualificationWorkAdmin(admin.ModelAdmin):
    fields = ("full_name", "topic_of_work", "scientific_supervisor")
    list_display = ('topic_of_work',)
    list_per_page = 10
    search_fields = ('topic_of_work',)