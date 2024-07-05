from django.db import models
from profiles.models import Profile

class Chatbot(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    faq = models.TextField(blank=True)
    about_me = models.TextField(blank=True)
    work_examples = models.TextField(blank=True)
    schedule = models.TextField(blank=True)

    def __str__(self):
        return f"Chatbot for {self.profile.user.username}"
