from django.db import models
from profiles.models import Profile

class Project(models.Model):
    is_published = models.BooleanField(default=False)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    link = models.URLField(blank=True, null=True)
    image1 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image2 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image3 = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title
