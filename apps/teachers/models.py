from django.db import models

from apps.positions.models import Positions


class Teachers(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    photo = models.BinaryField(null=True)

    class Meta:
        db_table = 'Teachers'

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'