from django.db import models

from django.utils.text import slugify
from unidecode import unidecode

from employees.models import Employee


class EducationalDegreeDetailsFiles(models.Model):

    file = models.FileField(upload_to='educational_degrees_files/', verbose_name="Файл")
    name = models.CharField(max_length=255, verbose_name="Назва файла")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Файл опису наукового ступіня: {self.name}"

    class Meta:
        verbose_name = "Файл опису наукового ступіня"
        verbose_name_plural = "Файли опису наукового ступіня"


class EducationalDegreeStudyProgramsFiles(models.Model):
    file = models.FileField(upload_to='educational_degrees_files/', verbose_name="Файл")
    name = models.CharField(max_length=255, verbose_name="Назва файла")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Файл освітньої програми: {self.name}"

    class Meta:
        verbose_name = "Файл освітньої програми"
        verbose_name_plural = "Файли освітніх програм"


class EducationalDegreeStudyPlansFiles(models.Model):
    file = models.FileField(upload_to='educational_degrees_files/', verbose_name="Файл")
    name = models.CharField(max_length=255, verbose_name="Назва файла")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Файл навчального плану: {self.name}"

    class Meta:
        verbose_name = "Файл навчального плану"
        verbose_name_plural = "Файли навчальних планів"


class EducationalDegreeDisciplineProgramsFiles(models.Model):
    file = models.FileField(upload_to='educational_degrees_files/', verbose_name="Файл")
    name = models.CharField(max_length=255, verbose_name="Назва файла")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Файл освітньої дисциплини: {self.name}"

    class Meta:
        verbose_name = "Файл освітньої дисциплини"
        verbose_name_plural = "Файли освітніх дисциплин"


class QualificationWork(models.Model):
    full_name = models.CharField(max_length=255, verbose_name="ПІБ студента")
    topic_of_work = models.CharField(verbose_name="Тема кваліфікаційної роботи")

    scientific_supervisor = models.ForeignKey(to=Employee,
                                              on_delete=models.SET_NULL,
                                              null=True,
                                              blank=True,
                                              related_name="scientific_supervisors",
                                              related_query_name="scientific_supervisor",
                                              verbose_name="Науковий керівник")

    def __str__(self):
        return f"Кваліфікаційна робота {self.full_name} "

    class Meta:
        verbose_name = "Кваліфікаційна робота"
        verbose_name_plural = "Кваліфікаційні роботи"


class EducationalDegreeQualificationWorks(models.Model):
    year = models.CharField(max_length=255, verbose_name="Рік")
    slug = models.SlugField(max_length=300, verbose_name="Слаг", allow_unicode=True)
    degree_name = models.CharField(max_length=255, verbose_name="Назва освітнього ступеня")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    qualification_work = models.ManyToManyField(QualificationWork,
                                                 verbose_name="Кваліфікаційні роботи",
                                                 related_name="qualification_works",
                                                 related_query_name="qualification_work",
                                                 blank=True
                                                 )

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        latinic_name = unidecode(self.year) + '-' + unidecode(self.degree_name)
        self.slug = slugify(latinic_name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return f"Кваліфікаційні роботи {self.degree_name} {self.year}"

    class Meta:
        verbose_name = "Список кваліфікаційних робіт"
        verbose_name_plural = "Списки кваліфікаційних робіт"


class EducationalDegree(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва освітнього ступіня")
    description = models.TextField(verbose_name="Опис освітнього ступіня")
    slug = models.SlugField(max_length=300, verbose_name="Слаг", allow_unicode=True)

    detailed_info = models.ManyToManyField(EducationalDegreeDetailsFiles,
                                           verbose_name="Описи освітнього ступіня",
                                           related_name="detailed_info_files",
                                           related_query_name="detailed_info_file",
                                           blank=True
                                           )
    study_programs_desc = models.ManyToManyField(EducationalDegreeStudyProgramsFiles,
                                                 verbose_name="Описи освітньої програми",
                                                 related_name="study_programs",
                                                 related_query_name="study_program",
                                                 blank=True
                                                 )
    study_plans = models.ManyToManyField(EducationalDegreeStudyPlansFiles,
                                         verbose_name="Навчальні плани",
                                         related_name="study_plans",
                                         related_query_name="study_plan",
                                         blank=True
                                         )
    disciplines_programs = models.ManyToManyField(EducationalDegreeDisciplineProgramsFiles,
                                                  verbose_name="Програми навчальних дисциплін",
                                                  related_name="disciplines_programs",
                                                  related_query_name="discipline_program",
                                                  blank=True
                                                  )
    qualification_works = models.ManyToManyField(EducationalDegreeQualificationWorks,
                                                 verbose_name="Кваліфікаційні роботи",
                                                 related_name="qualification_works_lists",
                                                 related_query_name="qualification_work_list",
                                                 blank=True
                                                 )

    def __str__(self):
        return f"Освітній ступінь: {self.name}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        latinic_name = unidecode(self.name)
        self.slug = slugify(latinic_name, allow_unicode=True)
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = "Освітній ступінь"
        verbose_name_plural = "Освітні ступені"
        constraints = (models.UniqueConstraint(fields=('name',), name='educational_degree_name_unique_constraint'),
                       models.UniqueConstraint(fields=('slug',), name='educational_degree_slug_unique_constraint'))
        indexes = (models.Index(fields=('slug',), name='educational_degree_slug_index'),
                   )