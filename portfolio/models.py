from django.db import models
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField


languages = (
    ('HTML', 'HTML'), ('CSS', 'CSS'), ('JavaScript', 'JavaScript'),
    ('Bootstrap', 'Bootstrap'), ('jQuery', 'jQuery'), ('Python', 'Python')

)


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    programing_languages = MultiSelectField(choices=languages)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
