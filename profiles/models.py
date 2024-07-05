from django.db import models
from django.conf import settings

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    phone = models.CharField(max_length=15, null=True, blank=True)
    full_name = models.CharField(max_length=255)
    headline = models.CharField(max_length=255)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    template = models.PositiveIntegerField(default=1)
    facebook_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)  # x.com link
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    tiktok_link = models.URLField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    behance_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.full_name} Profile'
