from django.db import models

class EducationForms(models.Model):
    name = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'EducationForms'