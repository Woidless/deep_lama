from django.db import models

from apps.subjects.models import Subjects
from apps.account.models import CustomUser


class AdditionalMaterials(models.Model):
    name = models.CharField(max_length=255, null=True)
    type = models.CharField(max_length=255, null=True)
    file_link = models.CharField(max_length=255, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'AdditionalMaterials'

    def __str__(self):
        return self.name