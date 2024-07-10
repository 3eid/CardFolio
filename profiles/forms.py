from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['is_published', 'full_name', 'headline', 'bio', 'profile_pic', 'email', 'website', 
                  'facebook_link', 'twitter_link', 'linkedin_link', 'instagram_link', 'tiktok_link', 
                  'youtube_link', 'github_link', 'behance_link']
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'headline': forms.TextInput(attrs={'class': 'form-control'}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'profile_pic': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_link': forms.URLInput(attrs={'class': 'form-control'}),
            'twitter_link': forms.URLInput(attrs={'class': 'form-control'}),
            'linkedin_link': forms.URLInput(attrs={'class': 'form-control'}),
            'instagram_link': forms.URLInput(attrs={'class': 'form-control'}),
            'tiktok_link': forms.URLInput(attrs={'class': 'form-control'}),
            'youtube_link': forms.URLInput(attrs={'class': 'form-control'}),
            'github_link': forms.URLInput(attrs={'class': 'form-control'}),
            'behance_link': forms.URLInput(attrs={'class': 'form-control'}),
            }