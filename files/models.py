from django.db import models


class File(models.Model):
    filename = models.TextField()
    path = models.TextField()
