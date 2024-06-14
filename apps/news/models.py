from django.db import models

class News(models.Model):
    headline = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    publication_date = models.DateField(null=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    class Meta:
        db_table = 'News'