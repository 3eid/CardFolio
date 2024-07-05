from django.db import models
from profiles.models import Profile

class Article(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    heading = models.CharField(max_length=255,null=True)
    subheading = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.heading
