from django.db import models

from apps.subjects.models import Subjects
from apps.teachers.models import Teachers


class TeacherSubjects(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('teacher', 'subject'),)
        db_table = 'TeacherSubjects'
