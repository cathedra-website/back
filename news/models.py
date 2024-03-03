from django.db import models
from files.models import File


class News(models.Model):
    title = models.CharField(blank=False, max_length=255)
    content = models.TextField()
    image_id = models.ForeignKey(File, on_delete=models.SET_NULL, null=True)
    src_link = models.TextField()
