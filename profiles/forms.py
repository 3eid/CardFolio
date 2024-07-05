from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_published', 'full_name', 'headline', 'bio', 'profile_pic', 'email', 'website', 'template', 
                  'facebook_link', 'twitter_link', 'linkedin_link', 'instagram_link', 'tiktok_link', 
                  'youtube_link', 'github_link', 'behance_link']
