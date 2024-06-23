# additionalMaterialType/models.py
from django.db import models

class AdditionalMaterialType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AdditionalMaterialType'
