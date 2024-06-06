from django.db import models

from apps.subjects.models import Subjects


class WebMaterials(models.Model):
    name = models.CharField(max_length=255, null=True)
    web_link = models.CharField(max_length=255, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'WebMaterials'
