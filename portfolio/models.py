from django.db import models
from ckeditor.fields import RichTextField


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
