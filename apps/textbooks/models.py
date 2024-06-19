from django.db import models
from apps.subjects.models import Subjects

class Textbooks(models.Model):
    name = models.CharField(max_length=255, null=True)
    quantity = models.IntegerField(default=0)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'Textbooks'

    def __str__(self):
        return self.name