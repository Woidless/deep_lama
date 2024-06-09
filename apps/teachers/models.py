from django.db import models

from apps.positions.models import Positions


class Teachers(models.Model):
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.ForeignKey(Positions, on_delete=models.CASCADE)
    photo = models.BinaryField(null=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'Teachers'