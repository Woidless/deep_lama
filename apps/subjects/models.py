from django.db import models

from apps.educationForms.models import EducationForms
from apps.studyCycles.models import StudyCycles


class Subjects(models.Model):
    name = models.CharField(max_length=255, null=True)
    education_form = models.ForeignKey(EducationForms, on_delete=models.CASCADE, null=True)
    study_cycle = models.ForeignKey(StudyCycles, on_delete=models.CASCADE, null=True)
    number_of_students = models.IntegerField(null=True)

    class Meta:
        db_table = 'Subjects'
