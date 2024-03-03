from django.db import models
from django.utils import timezone
from files.models import File


# TODO: Have to be changed to the view of the JSON
def links_default():
    """Default json style for Employee.links"""
    return {}


class Position(models.Model):
    role = models.TextField()


class Employee(models.Model):
    first_name = models.CharField(blank=False, max_length=255)
    last_name = models.CharField(blank=False, max_length=255)
    middle_name = models.CharField(blank=False, max_length=255)
    email = models.EmailField()
    ranks = models.TextField()
    links = models.JSONField(default=links_default)
    degree_history = models.TextField()
    study_interests = models.TextField()
    diploma_work_topics = models.TextField()
    position_id = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    image_id = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.TextField()

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)
        self.created_at = self.created_at

    def save(self, *args, **kwargs):
        # TODO: Is it work?
        if not self.created_at and self.created_at:
            self.updated_at = timezone.now()
        super(Employee, self).save(*args, **kwargs)


class TeachDiscipline(models.Model):
    name = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(TeachDiscipline, self).__init__(*args, **kwargs)
        self.created_at = self.created_at

    def save(self, *args, **kwargs):
        # TODO: Is it work?
        if not self.created_at and self.created_at:
            self.updated_at = timezone.now()
        super(TeachDiscipline, self).save(*args, **kwargs)


class EmployeeTeachDiscipline(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    discipline_id = models.ForeignKey(TeachDiscipline, on_delete=models.CASCADE)


class ScientificWorkType(models.Model):
    name = models.TextField()


class ScientificWork(models.Model):
    name = models.TextField()
    publishing_house = models.TextField()
    size = models.IntegerField()
    language = models.CharField(max_length=255)
    isbn = models.TextField()
    image_id = models.ForeignKey(
        File, related_name="scientific_work_image", on_delete=models.SET_NULL, null=True
    )
    file_id = models.ForeignKey(
        File, related_name="scientific_work_file", on_delete=models.SET_NULL, null=True
    )
    type_id = models.ForeignKey(
        ScientificWorkType, on_delete=models.SET_NULL, null=True
    )
    coworkers = models.TextField()
    description = models.TextField()


class ScientificWorkCoworker(models.Model):
    sceintific_work_id = models.ForeignKey(ScientificWork, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)


class ChosenPublication(models.Model):
    scientific_word_id = models.ForeignKey(ScientificWork, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
