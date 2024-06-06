from django.db import models
from apps.subjects.models import Subjects
from apps.textbooks.models import Textbooks
from apps.webMaterials.models import WebMaterials

class SubjectDetails(models.Model):
    study_cycle = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    education_form = models.CharField(max_length=255)
    number_of_students = models.IntegerField()
    textbooks = models.ManyToManyField(Textbooks, related_name='subject_details_textbooks')
    web_materials = models.ManyToManyField(WebMaterials, related_name='subject_details')

    def __str__(self):
        return f"{self.study_cycle} - {self.subject}"

    class Meta:
        db_table = 'SubjectDetails'
