from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['heading', 'subheading', 'description', 'image', 'is_published']
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            
            'subheading': forms.TextInput(attrs={'class': 'form-control'}),
            
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows':4 }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }